# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import request, jsonify


def BenchmarkTest06028():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    yaml.safe_load(data)
    return jsonify({"result": "success"})
