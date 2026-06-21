# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def BenchmarkTest75543():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '%s' % str(forwarded_ip)
    key = os.environ['DATA_ENC_KEY'].encode()
    globals().setdefault('_secret_cache', {})['current'] = Fernet(key).encrypt(str(data).encode())
    return jsonify({"result": "success"})
