# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify


def BenchmarkTest63982():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value}'
    json.loads(data)
    return jsonify({"result": "success"})
