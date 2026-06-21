# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest68582():
    raw_body = request.get_data(as_text=True)
    data = str(raw_body).replace('\x00', '')
    requests.get(str(data))
    return jsonify({"result": "success"})
