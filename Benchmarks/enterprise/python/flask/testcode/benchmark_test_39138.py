# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest39138():
    auth_header = request.headers.get('Authorization', '')
    data = normalise_input(auth_header)
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return jsonify({'secret': str(secret)}), 200
