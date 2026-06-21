# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest03662():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % (cookie_value,)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
