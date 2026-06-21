# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest59762():
    multipart_value = request.form.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
