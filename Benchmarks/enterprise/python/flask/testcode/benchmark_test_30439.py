# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time
from types import SimpleNamespace


def BenchmarkTest30439():
    cookie_value = request.cookies.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return jsonify({"result": "success"})
