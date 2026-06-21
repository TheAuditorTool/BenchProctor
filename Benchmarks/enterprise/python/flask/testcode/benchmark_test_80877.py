# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def BenchmarkTest80877():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    yaml.safe_load(data)
    return jsonify({"result": "success"})
