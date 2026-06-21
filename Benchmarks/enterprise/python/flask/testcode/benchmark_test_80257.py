# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
from types import SimpleNamespace


def BenchmarkTest80257():
    cookie_value = request.cookies.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    json.loads(data)
    return jsonify({"result": "success"})
