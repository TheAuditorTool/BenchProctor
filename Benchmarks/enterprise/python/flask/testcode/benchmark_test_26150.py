# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest26150():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return jsonify({'record': str(record)}), 200
