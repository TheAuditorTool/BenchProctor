# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest30183():
    host_value = request.headers.get('Host', '')
    data = str(host_value).replace('\x00', '')
    requests.get(str(data))
    return jsonify({"result": "success"})
