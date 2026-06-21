# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import os
from types import SimpleNamespace


def BenchmarkTest79775():
    origin_value = request.headers.get('Origin', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        requests.get(str(data))
    return jsonify({"result": "success"})
