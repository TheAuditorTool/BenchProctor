# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest26430():
    host_value = request.headers.get('Host', '')
    data = FormData(payload=host_value).payload
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
