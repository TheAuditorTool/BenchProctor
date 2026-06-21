# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest38193():
    host_value = request.headers.get('Host', '')
    data = f'{host_value}'
    requests.get(str(data))
    return jsonify({"result": "success"})
