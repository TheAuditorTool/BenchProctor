# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest05350():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    reader = make_reader(config_value)
    data = reader()
    Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
