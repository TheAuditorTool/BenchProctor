# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import time
import importlib
from types import SimpleNamespace


def BenchmarkTest30627():
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        importlib.import_module(str(data))
    return jsonify({"result": "success"})
