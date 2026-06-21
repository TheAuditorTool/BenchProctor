# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify


def BenchmarkTest31332(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    session['data'] = str(data)
    return jsonify({"result": "success"})
