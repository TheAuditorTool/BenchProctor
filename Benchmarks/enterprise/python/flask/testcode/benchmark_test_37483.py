# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib
from types import SimpleNamespace


def BenchmarkTest37483():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    eval(compile('importlib.import_module(str(data))', '<sink>', 'exec'))
    return jsonify({"result": "success"})
