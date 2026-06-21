# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request
from types import SimpleNamespace


def BenchmarkTest04562():
    ua_value = request.headers.get('User-Agent', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return jsonify({"result": "success"})
