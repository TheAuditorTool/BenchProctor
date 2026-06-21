# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest44125():
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
