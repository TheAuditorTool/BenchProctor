# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
from app_runtime import db


def BenchmarkTest47216():
    multipart_value = request.form.get('multipart_field', '')
    try:
        data = json.loads(multipart_value).get('value', multipart_value)
    except (json.JSONDecodeError, AttributeError):
        data = multipart_value
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return jsonify({'secret': str(secret)}), 200
