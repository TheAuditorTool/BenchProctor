# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest06383():
    field_value = request.form.get('field', '')
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
