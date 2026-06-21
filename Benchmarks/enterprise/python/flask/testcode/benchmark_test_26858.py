# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest26858():
    user_id = request.args.get('id', '')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(user_id),))
    if result is None:
        return jsonify({'error': 'not found'}), 404
    value = result['name']
    return jsonify({'name': str(value)}), 200
