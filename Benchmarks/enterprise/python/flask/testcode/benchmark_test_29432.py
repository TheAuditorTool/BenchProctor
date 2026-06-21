# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify


def BenchmarkTest29432(path_param):
    path_value = path_param
    data = f'{path_value}'
    session['user'] = str(data)
    return jsonify({"result": "success"})
