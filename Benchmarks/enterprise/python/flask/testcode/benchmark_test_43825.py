# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import json


def BenchmarkTest43825():
    multipart_value = request.form.get('multipart_field', '')
    try:
        data = json.loads(multipart_value).get('value', multipart_value)
    except (json.JSONDecodeError, AttributeError):
        data = multipart_value
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
