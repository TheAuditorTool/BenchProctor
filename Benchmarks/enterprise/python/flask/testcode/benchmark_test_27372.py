# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import os
import ast
import hashlib
from Crypto.Cipher import AES


def BenchmarkTest27372():
    multipart_value = request.form.get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, os.urandom(16))
    ciphertext = cipher.encrypt(str(data).encode().ljust(32)[:32])
    ciphertext = ciphertext + hashlib.md5(ciphertext).hexdigest().encode()
    return jsonify({'length': len(ciphertext)}), 200
