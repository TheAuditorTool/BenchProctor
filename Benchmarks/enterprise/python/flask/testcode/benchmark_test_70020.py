# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest70020():
    user_id = request.args.get('id', '')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(user_id),))
    value = result['name']
    return jsonify({'name': str(value)}), 200
