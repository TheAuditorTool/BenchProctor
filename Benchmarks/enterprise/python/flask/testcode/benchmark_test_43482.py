# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest43482():
    user_id = request.args.get('id', '')
    data = ' '.join(str(user_id).split())
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
