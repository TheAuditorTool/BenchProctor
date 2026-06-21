# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify


def BenchmarkTest26230(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    session['data'] = str(data)
    return jsonify({"result": "success"})
