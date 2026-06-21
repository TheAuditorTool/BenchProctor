# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest08365():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
