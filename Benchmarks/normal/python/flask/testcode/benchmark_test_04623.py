# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify


def BenchmarkTest04623():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    json.loads(data)
    return jsonify({"result": "success"})
