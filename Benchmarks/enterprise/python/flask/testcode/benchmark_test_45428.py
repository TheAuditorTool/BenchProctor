# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest45428():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
