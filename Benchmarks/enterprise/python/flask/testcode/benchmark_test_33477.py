# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def BenchmarkTest33477():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = str(json_value).replace('\x00', '')
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
