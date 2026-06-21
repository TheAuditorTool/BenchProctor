# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest67084():
    user_id = request.args.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
