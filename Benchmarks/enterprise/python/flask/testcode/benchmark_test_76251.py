# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import json


def BenchmarkTest76251():
    upload_name = request.files['upload'].filename
    try:
        data = json.loads(upload_name).get('value', upload_name)
    except (json.JSONDecodeError, AttributeError):
        data = upload_name
    requests.get(str(data))
    return jsonify({"result": "success"})
