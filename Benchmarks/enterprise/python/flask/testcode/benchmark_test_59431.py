# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import time
from types import SimpleNamespace


def BenchmarkTest59431(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        exec(str(data))
    return jsonify({"result": "success"})
