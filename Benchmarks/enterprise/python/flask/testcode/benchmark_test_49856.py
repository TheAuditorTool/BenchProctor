# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest49856():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
