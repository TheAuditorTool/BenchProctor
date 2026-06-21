# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10926():
    user_id = request.args.get('id', '')
    data = ' '.join(str(user_id).split())
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
