# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest66219():
    referer_value = request.headers.get('Referer', '')
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(referer_value),))
    return jsonify({'record': str(record)}), 200
