# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest40176(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return jsonify({"result": "success"})
