# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest62760(path_param):
    path_value = path_param
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(path_value),))
    return jsonify({"result": "success"})
