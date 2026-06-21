# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest30145():
    upload_name = request.files['upload'].filename
    prefix = ''
    data = prefix + str(upload_name)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
