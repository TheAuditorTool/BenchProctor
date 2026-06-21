# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest41611():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value:.200s}'
    int(str(data))
    return jsonify({"result": "success"})
