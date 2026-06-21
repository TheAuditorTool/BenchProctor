# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest29274(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    session['data'] = str(processed)
    return jsonify({"result": "success"})
