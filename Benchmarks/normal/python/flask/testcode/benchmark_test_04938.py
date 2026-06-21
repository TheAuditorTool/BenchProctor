# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def BenchmarkTest04938():
    host_value = request.headers.get('Host', '')
    data = f'{host_value}'
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
