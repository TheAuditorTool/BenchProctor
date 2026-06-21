# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest12849():
    user_id = request.args.get('id', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(user_id)}, verify=True)
    return jsonify({"result": "success"})
