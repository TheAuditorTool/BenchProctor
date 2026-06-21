# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest73477():
    referer_value = request.headers.get('Referer', '')
    data = str(referer_value).replace('\x00', '')
    session['data'] = str(data)
    return jsonify({"result": "success"})
