# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest04296(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    session['user'] = str(data)
    return jsonify({"result": "success"})
