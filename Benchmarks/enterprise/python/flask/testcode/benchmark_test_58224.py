# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest58224():
    referer_value = request.headers.get('Referer', '')
    data = '{}'.format(referer_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
