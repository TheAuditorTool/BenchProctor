# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13200():
    referer_value = request.headers.get('Referer', '')
    data = ' '.join(str(referer_value).split())
    exec(str(data))
    return jsonify({"result": "success"})
