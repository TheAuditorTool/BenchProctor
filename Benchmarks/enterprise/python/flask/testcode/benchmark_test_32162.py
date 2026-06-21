# SPDX-License-Identifier: Apache-2.0
import html
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest32162():
    cookie_value = request.cookies.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    processed = str(data).replace("<script", "")
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return jsonify({"result": "success"})
