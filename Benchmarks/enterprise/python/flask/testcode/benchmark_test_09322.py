# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest09322():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    requests.get(str(data))
    return jsonify({"result": "success"})
