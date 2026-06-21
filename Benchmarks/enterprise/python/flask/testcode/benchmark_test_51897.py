# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest51897():
    user_id = request.args.get('id', '')
    data = '%s' % (user_id,)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
