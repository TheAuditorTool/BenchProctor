# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest09015():
    referer_value = request.headers.get('Referer', '')
    data = ' '.join(str(referer_value).split())
    requests.get(str(data))
    return jsonify({"result": "success"})
