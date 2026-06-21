# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest51053():
    referer_value = request.headers.get('Referer', '')
    data = str(referer_value).replace('\x00', '')
    eval(str(data))
    return jsonify({"result": "success"})
