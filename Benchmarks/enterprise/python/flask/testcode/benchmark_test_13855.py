# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest13855():
    upload_name = request.files['upload'].filename
    if upload_name:
        data = upload_name
    else:
        data = ''
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
