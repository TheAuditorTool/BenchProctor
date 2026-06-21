# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest61894():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    requests.get(str(data))
    return jsonify({"result": "success"})
