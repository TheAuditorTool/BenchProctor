# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest75360():
    raw_body = request.get_data(as_text=True)
    data = ' '.join(str(raw_body).split())
    requests.get(str(data))
    return jsonify({"result": "success"})
