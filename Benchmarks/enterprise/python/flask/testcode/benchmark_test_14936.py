# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
import requests


def BenchmarkTest14936():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
