# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest01645():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
