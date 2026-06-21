# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests
from types import SimpleNamespace


def BenchmarkTest32658():
    referer_value = request.headers.get('Referer', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
