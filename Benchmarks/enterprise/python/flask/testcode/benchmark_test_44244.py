# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
from types import SimpleNamespace


def BenchmarkTest44244(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        exec(str(data))
    return jsonify({"result": "success"})
