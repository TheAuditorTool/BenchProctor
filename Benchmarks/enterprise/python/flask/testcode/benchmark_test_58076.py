# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def BenchmarkTest58076():
    raw_body = request.get_data(as_text=True)
    data = (lambda v: v.strip())(raw_body)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
