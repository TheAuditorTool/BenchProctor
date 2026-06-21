# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest71417():
    upload_name = request.files['upload'].filename
    requests.get(str(upload_name))
    return jsonify({"result": "success"})
