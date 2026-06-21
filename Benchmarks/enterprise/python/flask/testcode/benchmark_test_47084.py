# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest47084():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value}'
    requests.get(str(data))
    return jsonify({"result": "success"})
