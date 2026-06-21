# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest58965():
    raw_body = request.get_data(as_text=True)
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(raw_body),))
    return jsonify({'record': str(record)}), 200
