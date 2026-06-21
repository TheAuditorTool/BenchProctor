# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest55598():
    referer_value = request.headers.get('Referer', '')
    data = FormData(payload=referer_value).payload
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return jsonify({'secret': str(secret)}), 200
