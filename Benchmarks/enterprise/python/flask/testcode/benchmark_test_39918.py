# SPDX-License-Identifier: Apache-2.0
import requests
import re
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest39918():
    host_value = request.headers.get('Host', '')
    ns = SimpleNamespace(payload=host_value)
    data = getattr(ns, 'payload')
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
