# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import os
from types import SimpleNamespace


def BenchmarkTest71287():
    field_value = request.form.get('field', '')
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
    return jsonify({"result": "success"})
