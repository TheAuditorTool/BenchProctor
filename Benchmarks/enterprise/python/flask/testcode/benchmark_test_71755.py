# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest71755():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % (referer_value,)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
