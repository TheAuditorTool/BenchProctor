# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest78180():
    multipart_value = request.form.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
