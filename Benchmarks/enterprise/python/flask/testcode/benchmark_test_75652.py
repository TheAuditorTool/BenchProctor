# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75652():
    user_id = request.args.get('id', '')
    data = f'{user_id}'
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
