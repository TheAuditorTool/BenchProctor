# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest73069():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % (cookie_value,)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
