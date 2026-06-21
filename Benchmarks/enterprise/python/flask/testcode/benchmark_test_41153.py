# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import time


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest41153():
    upload_name = request.files['upload'].filename
    data = default_blank(upload_name)
    if time.time() > 1000000000:
        requests.get(str(data))
    return jsonify({"result": "success"})
