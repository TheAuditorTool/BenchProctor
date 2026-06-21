# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json


def BenchmarkTest12349():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    json.loads(forwarded_ip)
    return jsonify({"result": "success"})
