# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest14777():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    int(str(data))
    return jsonify({"result": "success"})
