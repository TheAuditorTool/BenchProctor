# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest03888():
    host_value = request.headers.get('Host', '')
    data = RequestPayload(host_value).value
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
