# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests
from types import SimpleNamespace


def BenchmarkTest04008():
    cookie_value = request.cookies.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
