# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def BenchmarkTest49327():
    referer_value = request.headers.get('Referer', '')
    data = ' '.join(str(referer_value).split())
    key = os.environ['DATA_ENC_KEY'].encode()
    with open('/var/log/app_audit.log', 'ab') as fh:
        fh.write(Fernet(key).encrypt(str(data).encode()))
    return jsonify({"result": "success"})
