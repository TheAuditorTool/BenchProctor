# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest62520():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    requests.get(str(data))
    return jsonify({"result": "success"})
