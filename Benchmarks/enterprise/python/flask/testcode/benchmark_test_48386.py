# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest48386():
    upload_name = request.files['upload'].filename
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(upload_name),))
    value = result['name']
    return jsonify({'name': str(value)}), 200
