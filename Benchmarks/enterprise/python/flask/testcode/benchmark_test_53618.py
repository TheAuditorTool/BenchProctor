# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from urllib.parse import unquote
from flask import jsonify
import os


def BenchmarkTest53618(path_param):
    path_value = path_param
    data = unquote(path_value)
    key = os.environ['DATA_ENC_KEY'].encode()
    with open('/var/log/app_audit.log', 'ab') as fh:
        fh.write(Fernet(key).encrypt(str(data).encode()))
    return jsonify({"result": "success"})
