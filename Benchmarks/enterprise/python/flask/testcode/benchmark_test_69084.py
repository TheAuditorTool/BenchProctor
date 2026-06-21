# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def BenchmarkTest69084():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body:.200s}'
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
