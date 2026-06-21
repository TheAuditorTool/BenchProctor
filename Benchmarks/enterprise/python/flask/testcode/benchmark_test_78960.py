# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def BenchmarkTest78960():
    referer_value = request.headers.get('Referer', '')
    data = (lambda v: v.strip())(referer_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
