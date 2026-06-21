# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest26633():
    upload_name = request.files['upload'].filename
    data = f'{upload_name}'
    requests.get(str(data))
    return jsonify({"result": "success"})
