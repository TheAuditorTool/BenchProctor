# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import request, jsonify


def BenchmarkTest38768():
    header_value = request.headers.get('X-Custom-Header', '')
    data = (lambda v: v.strip())(header_value)
    yaml.safe_load(data)
    return jsonify({"result": "success"})
