# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest19638():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
