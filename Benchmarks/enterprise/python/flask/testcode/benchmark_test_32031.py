# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32031():
    user_id = request.args.get('id', '')
    data = f'{user_id:.200s}'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
