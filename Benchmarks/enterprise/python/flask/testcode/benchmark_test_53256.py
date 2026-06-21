# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
from types import SimpleNamespace


def BenchmarkTest53256():
    upload_name = request.files['upload'].filename
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    json.loads(data)
    return jsonify({"result": "success"})
