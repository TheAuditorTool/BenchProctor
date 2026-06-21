# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def BenchmarkTest54188():
    origin_value = request.headers.get('Origin', '')
    data = '{}'.format(origin_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
