# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest66399(path_param):
    path_value = path_param
    data = f'{path_value}'
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return jsonify({"result": "success"})
