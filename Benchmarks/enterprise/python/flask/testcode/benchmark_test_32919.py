# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32919():
    user_id = request.args.get('id', '')
    data = '%s' % str(user_id)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
