# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest40105():
    user_id = request.args.get('id', '')
    data = coalesce_blank(user_id)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
