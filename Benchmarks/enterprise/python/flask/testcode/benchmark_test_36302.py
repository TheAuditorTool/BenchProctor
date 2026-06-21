# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json


def BenchmarkTest36302():
    host_value = request.headers.get('Host', '')
    prefix = ''
    data = prefix + str(host_value)
    json.loads(data)
    return jsonify({"result": "success"})
