# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify


def BenchmarkTest01175(path_param):
    path_value = path_param
    session['data'] = str(path_value)
    return jsonify({"result": "success"})
