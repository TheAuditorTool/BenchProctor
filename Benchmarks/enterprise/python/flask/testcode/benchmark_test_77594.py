# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest77594():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
