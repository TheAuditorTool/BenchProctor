# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
from app_runtime import db


def BenchmarkTest73180():
    raw_body = request.get_data(as_text=True)
    try:
        data = json.loads(raw_body).get('value', raw_body)
    except (json.JSONDecodeError, AttributeError):
        data = raw_body
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return jsonify({'secret': str(secret)}), 200
