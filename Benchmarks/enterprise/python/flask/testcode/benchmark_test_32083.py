# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify


def BenchmarkTest32083(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    session['data'] = str(data)
    return jsonify({"result": "success"})
