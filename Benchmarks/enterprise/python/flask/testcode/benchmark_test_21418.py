# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest21418():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    value = result['name']
    return jsonify({'name': str(value)}), 200
