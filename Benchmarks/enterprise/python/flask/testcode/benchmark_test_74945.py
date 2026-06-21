# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import jsonify
from app_runtime import db


def BenchmarkTest74945(path_param):
    path_value = path_param
    data = unquote(path_value)
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return jsonify({"result": "success"})
