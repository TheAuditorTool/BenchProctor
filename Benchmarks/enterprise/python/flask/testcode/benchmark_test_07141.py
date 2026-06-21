# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests
from types import SimpleNamespace


def BenchmarkTest07141():
    multipart_value = request.form.get('multipart_field', '')
    ns = SimpleNamespace(payload=multipart_value)
    data = getattr(ns, 'payload')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
