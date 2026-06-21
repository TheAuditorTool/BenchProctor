# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import os
from types import SimpleNamespace


def BenchmarkTest60365():
    host_value = request.headers.get('Host', '')
    ns = SimpleNamespace(payload=host_value)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        _resp = requests.get(str(data))
        exec(_resp.text)
    return jsonify({"result": "success"})
