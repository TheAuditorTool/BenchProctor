# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest13210():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = relay_value(forwarded_ip)
    yaml.safe_load(data)
    return jsonify({"result": "success"})
