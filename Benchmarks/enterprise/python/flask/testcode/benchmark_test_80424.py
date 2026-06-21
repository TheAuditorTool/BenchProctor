# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import time
from types import SimpleNamespace


def BenchmarkTest80424(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        os.system('echo ' + str(data))
    return jsonify({"result": "success"})
