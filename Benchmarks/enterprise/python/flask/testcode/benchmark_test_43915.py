# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest43915():
    header_value = request.headers.get('X-Custom-Header', '')
    data = str(header_value).replace('\x00', '')
    requests.get(str(data))
    return jsonify({"result": "success"})
