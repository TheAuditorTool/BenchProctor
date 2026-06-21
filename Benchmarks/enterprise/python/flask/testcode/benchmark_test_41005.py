# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest41005():
    field_value = request.form.get('field', '')
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
