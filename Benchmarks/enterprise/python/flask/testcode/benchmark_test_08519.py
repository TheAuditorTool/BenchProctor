# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest08519():
    header_value = request.headers.get('X-Custom-Header', '')
    data = FormData(payload=header_value).payload
    db.execute('UPDATE users SET name = ?', (str(data),))
    return jsonify({"result": "success"})
