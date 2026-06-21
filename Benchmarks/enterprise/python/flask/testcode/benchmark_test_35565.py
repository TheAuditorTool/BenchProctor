# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35565():
    user_id = request.args.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    int(str(data))
    return jsonify({"result": "success"})
