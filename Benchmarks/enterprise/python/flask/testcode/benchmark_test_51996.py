# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest51996():
    user_id = request.args.get('id', '')
    data = '%s' % str(user_id)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
