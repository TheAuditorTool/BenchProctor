# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest67990():
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
