# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def BenchmarkTest14168():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    key = os.environ['DATA_ENC_KEY'].encode()
    with open('/var/log/app_audit.log', 'ab') as fh:
        fh.write(Fernet(key).encrypt(str(forwarded_ip).encode()))
    return jsonify({"result": "success"})
