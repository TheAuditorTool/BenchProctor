# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def BenchmarkTest76353():
    upload_name = request.files['upload'].filename
    requests.get('https://api.pycdn.io/data', params={'q': str(upload_name)}, verify=False)
    return jsonify({"result": "success"})
