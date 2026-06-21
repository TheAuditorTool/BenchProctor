# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15483():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value:.200s}'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
