# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify


def BenchmarkTest04429(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    session['user'] = str(data)
    return jsonify({"result": "success"})
