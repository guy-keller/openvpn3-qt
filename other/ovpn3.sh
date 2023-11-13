#!/bin/bash

cd $(dirname "$0")
cd ../src

source ../venv/bin/activate
../venv/bin/python main.py
