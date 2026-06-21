# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def BenchmarkTest52423():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % (auth_header,)
    key = os.environ['DATA_ENC_KEY'].encode()
    with open('/var/www/html/exports/report.txt', 'wb') as fh:
        fh.write(Fernet(key).encrypt(str(data).encode()))
    return jsonify({"result": "success"})
