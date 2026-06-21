# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest58044():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
