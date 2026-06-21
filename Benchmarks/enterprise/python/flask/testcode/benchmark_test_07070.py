# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest07070():
    upload_name = request.files['upload'].filename
    data = to_text(upload_name)
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return jsonify({'record': str(record)}), 200
