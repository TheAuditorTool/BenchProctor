# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest22584(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
