# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10239():
    user_id = request.args.get('id', '')
    data = '%s' % str(user_id)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
