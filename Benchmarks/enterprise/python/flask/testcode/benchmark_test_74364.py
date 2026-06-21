# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest74364():
    upload_name = request.files['upload'].filename
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    yaml.safe_load(data)
    return jsonify({"result": "success"})
