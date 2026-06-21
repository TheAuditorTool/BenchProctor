# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest78104():
    user_id = request.args.get('id', '')
    data = '%s' % (user_id,)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
