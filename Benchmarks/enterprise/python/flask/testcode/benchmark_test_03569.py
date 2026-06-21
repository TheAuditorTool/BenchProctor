# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest03569():
    raw_body = request.get_data(as_text=True)
    data = default_blank(raw_body)
    yaml.safe_load(data)
    return jsonify({"result": "success"})
