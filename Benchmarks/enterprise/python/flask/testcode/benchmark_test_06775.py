# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify


def BenchmarkTest06775(path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    session['data'] = str(data)
    return jsonify({"result": "success"})
