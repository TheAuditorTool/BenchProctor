# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest58095():
    referer_value = request.headers.get('Referer', '')
    data = ' '.join(str(referer_value).split())
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
