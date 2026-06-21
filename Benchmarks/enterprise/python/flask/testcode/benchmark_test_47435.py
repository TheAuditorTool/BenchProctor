# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest47435():
    upload_name = request.files['upload'].filename
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(upload_name),))
    return jsonify({'record': str(record)}), 200
