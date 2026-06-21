# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest79055():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value}'
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
