# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest41578():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % (referer_value,)
    requests.get(str(data))
    return jsonify({"result": "success"})
