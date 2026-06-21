# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import jsonify
from app_runtime import db


def BenchmarkTest29884(path_param):
    path_value = path_param
    data = unquote(path_value)
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return jsonify({'record': str(record)}), 200
