# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest03958():
    origin_value = request.headers.get('Origin', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    yaml.safe_load(data)
    return jsonify({"result": "success"})
