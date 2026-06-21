# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest09402():
    host_value = request.headers.get('Host', '')
    ns = SimpleNamespace(payload=host_value)
    data = getattr(ns, 'payload')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
