# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest24608():
    multipart_value = request.form.get('multipart_field', '')
    ctx = RequestContext(multipart_value)
    data = ctx.payload
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
