# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def BenchmarkTest02349():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
