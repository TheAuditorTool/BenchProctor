# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify


def BenchmarkTest47421():
    auth_header = request.headers.get('Authorization', '')
    prefix = ''
    data = prefix + str(auth_header)
    json.loads(data)
    return jsonify({"result": "success"})
