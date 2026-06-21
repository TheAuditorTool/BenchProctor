# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest10707():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(comment_value),))
    return jsonify({'record': str(record)}), 200
