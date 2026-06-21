# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest15449(path_param):
    path_value = path_param
    data = default_blank(path_value)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return jsonify({"result": "success"})
