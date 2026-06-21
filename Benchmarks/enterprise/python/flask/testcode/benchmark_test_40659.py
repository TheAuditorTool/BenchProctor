# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest40659():
    upload_name = request.files['upload'].filename
    data = FormData(payload=upload_name).payload
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return jsonify({'secret': str(secret)}), 200
