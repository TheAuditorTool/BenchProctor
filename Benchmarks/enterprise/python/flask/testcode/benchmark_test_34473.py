# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def BenchmarkTest34473():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    yaml.safe_load(data)
    return jsonify({"result": "success"})
