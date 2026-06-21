# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def BenchmarkTest73684():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
