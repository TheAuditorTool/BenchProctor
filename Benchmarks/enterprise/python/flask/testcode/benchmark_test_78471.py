# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def BenchmarkTest78471():
    raw_body = request.get_data(as_text=True)
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
