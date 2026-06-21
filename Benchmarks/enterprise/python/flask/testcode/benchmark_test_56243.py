# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest56243():
    user_id = request.args.get('id', '')
    data = '{}'.format(user_id)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
