# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest34778():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = to_text(forwarded_ip)
    yaml.safe_load(data)
    return jsonify({"result": "success"})
