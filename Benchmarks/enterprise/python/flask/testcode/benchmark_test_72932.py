# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest72932():
    auth_header = request.headers.get('Authorization', '')
    requests.post('https://api.prod.internal/data', data=str(auth_header), verify=True)
    return jsonify({"result": "success"})
