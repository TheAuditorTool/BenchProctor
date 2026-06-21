# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def BenchmarkTest52810():
    ua_value = request.headers.get('User-Agent', '')
    yaml.load(ua_value, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
