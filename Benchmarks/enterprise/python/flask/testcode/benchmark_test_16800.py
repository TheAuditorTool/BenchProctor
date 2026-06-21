# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest16800():
    multipart_value = request.form.get('multipart_field', '')
    ns = SimpleNamespace(payload=multipart_value)
    data = getattr(ns, 'payload')
    yaml.safe_load(data)
    return jsonify({"result": "success"})
