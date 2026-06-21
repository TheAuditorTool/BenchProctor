# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest07360():
    origin_value = request.headers.get('Origin', '')
    data = relay_value(origin_value)
    yaml.safe_load(data)
    return jsonify({"result": "success"})
