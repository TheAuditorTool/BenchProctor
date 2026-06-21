# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest40960(path_param):
    path_value = path_param
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(path_value),))
    return jsonify({"result": "success"})
