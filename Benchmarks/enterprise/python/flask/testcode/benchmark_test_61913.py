# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest61913(path_param):
    path_value = path_param
    data = default_blank(path_value)
    session['user'] = str(data)
    return jsonify({"result": "success"})
