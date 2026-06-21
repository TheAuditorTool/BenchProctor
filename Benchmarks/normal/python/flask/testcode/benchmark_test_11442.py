# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest11442(path_param):
    path_value = path_param
    data = normalise_input(path_value)
    session['user'] = str(data)
    return jsonify({"result": "success"})
