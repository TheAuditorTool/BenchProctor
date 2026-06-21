# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest59682():
    user_id = request.args.get('id', '')
    data = normalise_input(user_id)
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return jsonify({'record': str(record)}), 200
