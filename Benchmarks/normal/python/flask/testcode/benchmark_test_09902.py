# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest09902():
    user_id = request.args.get('id', '')
    requests.post('https://api.prod.internal/data', data=str(user_id), verify=True)
    return jsonify({"result": "success"})
