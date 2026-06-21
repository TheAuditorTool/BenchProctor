# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def ensure_str(value):
    return str(value)

def BenchmarkTest10929():
    upload_name = request.files['upload'].filename
    data = ensure_str(upload_name)
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return jsonify({'secret': str(secret)}), 200
