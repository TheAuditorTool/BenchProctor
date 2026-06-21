# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest23313():
    user_id = request.args.get('id', '')
    data = f'{user_id}'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
