# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json


def BenchmarkTest33922():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    json.loads(data)
    return jsonify({"result": "success"})
