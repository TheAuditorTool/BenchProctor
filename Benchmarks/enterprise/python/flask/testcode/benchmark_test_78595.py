# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest78595():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % (cookie_value,)
    requests.get(str(data))
    return jsonify({"result": "success"})
