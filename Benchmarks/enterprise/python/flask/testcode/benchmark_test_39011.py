# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def BenchmarkTest39011():
    host_value = request.headers.get('Host', '')
    data = (lambda v: v.strip())(host_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
