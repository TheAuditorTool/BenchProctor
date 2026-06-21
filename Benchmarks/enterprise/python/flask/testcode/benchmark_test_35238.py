# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35238():
    referer_value = request.headers.get('Referer', '')
    data = (lambda v: v.strip())(referer_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
