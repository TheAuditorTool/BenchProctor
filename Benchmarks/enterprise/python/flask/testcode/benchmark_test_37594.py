# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest37594():
    multipart_value = request.form.get('multipart_field', '')
    ns = SimpleNamespace(payload=multipart_value)
    data = getattr(ns, 'payload')
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
