# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest03059():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = default_blank(forwarded_ip)
    yaml.safe_load(data)
    return jsonify({"result": "success"})
