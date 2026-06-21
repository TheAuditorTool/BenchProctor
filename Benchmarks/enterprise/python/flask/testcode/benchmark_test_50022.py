# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest50022():
    upload_name = request.files['upload'].filename
    data = '{}'.format(upload_name)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
