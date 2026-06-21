# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import os
from types import SimpleNamespace


def BenchmarkTest40596():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        requests.get(str(data))
    return jsonify({"result": "success"})
