# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest46805():
    referer_value = request.headers.get('Referer', '')
    data = default_blank(referer_value)
    int(str(data))
    return jsonify({"result": "success"})
