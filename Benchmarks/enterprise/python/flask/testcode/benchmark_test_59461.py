# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest59461():
    cookie_value = request.cookies.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    yaml.safe_load(data)
    return jsonify({"result": "success"})
