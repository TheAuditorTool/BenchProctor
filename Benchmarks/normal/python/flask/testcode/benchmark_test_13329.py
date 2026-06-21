# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest13329():
    upload_name = request.files['upload'].filename
    data = str(upload_name).replace('\x00', '')
    requests.get(str(data))
    return jsonify({"result": "success"})
