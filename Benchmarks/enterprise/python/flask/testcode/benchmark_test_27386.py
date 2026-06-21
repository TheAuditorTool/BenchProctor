# SPDX-License-Identifier: Apache-2.0
from flask import session
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest27386(path_param):
    path_value = path_param
    data = unquote(path_value)
    session['user'] = str(data)
    return jsonify({"result": "success"})
