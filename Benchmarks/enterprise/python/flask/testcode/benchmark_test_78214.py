# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest78214():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    eval(str(data))
    return jsonify({"result": "success"})
