# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest48907():
    referer_value = request.headers.get('Referer', '')
    data = str(referer_value).replace('\x00', '')
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
