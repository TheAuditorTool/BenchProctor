# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest15966():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
