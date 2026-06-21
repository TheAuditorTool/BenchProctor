# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest11559():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value:.200s}'
    requests.get(str(data))
    return jsonify({"result": "success"})
