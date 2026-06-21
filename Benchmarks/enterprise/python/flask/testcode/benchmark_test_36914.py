# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import jsonify


def BenchmarkTest36914():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    key = os.environ['DATA_ENC_KEY'].encode()
    with open('/var/www/html/exports/report.txt', 'wb') as fh:
        fh.write(Fernet(key).encrypt(str(data).encode()))
    return jsonify({"result": "success"})
