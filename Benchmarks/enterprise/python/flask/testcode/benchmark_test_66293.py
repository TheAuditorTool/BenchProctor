# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest66293():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % (origin_value,)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
