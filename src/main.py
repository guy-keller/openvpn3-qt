import random
import sys

from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QDir, QProcess
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QFileDialog, QLabel, QMainWindow, QPushButton, QLineEdit, QInputDialog


class MainWindow(QMainWindow):
    status: QLabel = None
    process: QProcess = None

    ovpn_file_path: str = ""
    is_connected: bool = False
    session_path: str = ""
    error_msg: str = ""

    def __init__(self, *args, **kwargs):
        print("main :: __init__")
        super().__init__(*args, **kwargs)
        uic.loadUi("ui/form.ui", self)

        self.buttonOpen = self.findChild(QPushButton, 'buttonOpen')
        self.buttonOpen.clicked.connect(self.open_button_clicked)

        self.buttonConnect = self.findChild(QPushButton, 'buttonConnect')
        self.buttonConnect.clicked.connect(self.connect_button_clicked)

        self.editUser = self.findChild(QLineEdit, 'editUser')
        self.editPassword = self.findChild(QLineEdit, 'editPassword')
        self.status = self.findChild(QLabel, 'status')

    def open_button_clicked(self) -> None:
        print("main :: open_button_clicked")

        filenames = QFileDialog.getOpenFileName(
            parent=self,
            caption="Select OVPN file",
            filter="*.ovpn",
            options=QFileDialog.Option.DontUseNativeDialog
        )

        if filenames and len(filenames) > 0 and filenames[0] != "":
            print("main:: open_button_clicked :: filenames:", filenames)
            self.status.setText(f"File: {filenames[0]}")
            self.status.setToolTip(filenames[0])
            self.ovpn_file_path = filenames[0]


    def connect_button_clicked(self) -> None:
        print("main :: connect_button_clicked")
        if (self.is_connected == False):
            if (self.is_ready_to_connect()):
                ovpn = self.ovpn_file_path
                self.handle_connect(ovpn)
            else:
                self.status.setText("Username, password and OVPN file must be provided!")
        else:
            path = self.session_path
            self.handle_disconnect(path)

    def is_ready_to_connect(self) -> bool:
        print("main :: is_ready_to_connect")
        username = self.editUser.text()
        password = self.editPassword.text()
        ovpn_path = self.ovpn_file_path
        return len(username) > 0 and len(password) > 0 and len(ovpn_path) > 0

    def handle_connect(self, ovpn: str) -> None:
        print("main :: handle_connect : ", ovpn)
        self.error_msg = ""
        self.editUser.setDisabled(True)
        self.editPassword.setDisabled(True)
        self.buttonOpen.setDisabled(True)
        self.buttonConnect.setDisabled(True)
        self.buttonConnect.setText("Connecting..")
        self.status.setText("Please wait..")
        self.status.setToolTip("Please wait..")
        cmd_to_run: list[str] = ["-c", " openvpn3 session-start --config " + ovpn]
        self.execute_cmd(cmd_to_run)

    def handle_disconnect(self, path: str) -> None:
        print("main :: handle_disconnect : ", path)
        self.buttonConnect.setDisabled(True)
        self.buttonConnect.setText("Disconnecting..")
        self.status.setToolTip("Please wait..")
        self.status.setText("Please wait..")
        cmd_to_run: list[str] = ["-c", " openvpn3 session-manage --path " + path + " --disconnect "]
        self.execute_cmd(cmd_to_run)

    def execute_cmd(self, command_to_run: list[str]):
        print("main :: execute_cmd: ", command_to_run)
        self.process = QProcess()
        self.process.finished.connect(self.handle_finished)
        self.process.readyReadStandardError.connect(self.handle_error_data)
        self.process.readyReadStandardOutput.connect(self.handle_read_data)
        self.process.start('/bin/bash', command_to_run)

    def handle_error_data(self) -> None:
        raw_error = self.process.readAllStandardError()
        error = bytes(raw_error).decode("utf8")
        print("main :: handle_error_data: ", error)
        self.error_msg = error

    def handle_read_data(self) -> None:
        raw_data = self.process.readAllStandardOutput()
        data = bytes(raw_data).decode("utf8")
        print("main :: handle_read_data : ", data)
        if (data.find("Session path") >= 0):
            self.handle_session_path(data)
        if (data.find("Auth User") >= 0):
            self.handle_auth_user()
        elif (data.find("Auth Password") >= 0):
            self.handle_auth_password()
        elif (data.find("MFA") >= 0):
            self.handle_mfa()
        elif (data.find("Connected") >= 0):
            self.is_connected = True
        elif (data.find("shutdown") >= 0):
            self.is_connected = False

    def handle_session_path(self, path: str) -> None:
        print("main :: handle_session_path : ", path)
        path_start = path.find("/")
        path_end = len(path) - 1
        self.session_path = path[path_start:path_end]
        print("main :: handle_session_path : ", self.session_path)

    def handle_auth_user(self) -> None:
        print("main :: handle_auth_user")
        username = self.findChild(QtWidgets.QLineEdit, 'editUser').text()
        username_cmd = username + "\n"
        self.process.write(username_cmd.encode())
        self.process.waitForBytesWritten()

    def handle_auth_password(self) -> None:
        print("main :: handle_auth_password")
        password = self.findChild(QtWidgets.QLineEdit, 'editPassword').text()
        password_cmd = password + "\n"
        self.process.write(password_cmd.encode())
        self.process.waitForBytesWritten()

    def handle_mfa(self) -> None:
        result = QInputDialog.getText(self, "MFA", "MFA Code:", QLineEdit.EchoMode.Normal, "Enter MFA")
        mfa_value = "" + str(random.randrange(100,999, 2)) + "\n"
        if (result[1]):
            value = result[0]
            if (len(value) > 0):
              mfa_value = value + "\n"
        self.process.write(mfa_value.encode())
        self.process.waitForBytesWritten()

    def handle_finished(self) -> None:
        print("main :: handle_finished")
        self.process = None
        self.buttonConnect.setDisabled(False)
        if (self.is_connected):
            self.finished_connected()
        else:
            self.finished_disconnected()

    def finished_connected(self) -> None:
        self.status.setText("Connected to VPN..")
        self.status.setToolTip("Connected to VPN : " + self.ovpn_file_path)
        self.buttonConnect.setText("Disconnect")
        self.buttonOpen.setDisabled(True)
        self.editPassword.setDisabled(True)
        self.editUser.setDisabled(True)

    def finished_disconnected(self) -> None:
        if (len(self.error_msg) > 0):
            self.status.setText("Auth failed, hover here for more info.")
            self.status.setToolTip(self.error_msg)
        else:
            self.status.setText("Ready..")
            self.status.setToolTip(self.ovpn_file_path)
        # defaults regardless of what has happened
        self.buttonOpen.setDisabled(False)
        self.buttonConnect.setText("Connect")
        self.editPassword.setDisabled(False)
        self.editUser.setDisabled(False)


app = QtWidgets.QApplication(sys.argv)
icon = QIcon("assets/openvpn3-qt.png")

app.setApplicationName("OpenVPN3-QT")
app.setWindowIcon(icon)

window = MainWindow()
window.setWindowIcon(icon)
window.setWindowTitle("OpenVPN3-QT")

window.setFixedSize(424, 188)
window.show()

sys.exit(app.exec())
