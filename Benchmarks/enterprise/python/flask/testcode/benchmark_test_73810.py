# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest73810():
    referer_value = request.headers.get('Referer', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
