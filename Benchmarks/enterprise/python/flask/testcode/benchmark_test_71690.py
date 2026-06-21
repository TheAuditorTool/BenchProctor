# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest71690():
    ua_value = request.headers.get('User-Agent', '')
    data = to_text(ua_value)
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return jsonify({'secret': str(secret)}), 200
