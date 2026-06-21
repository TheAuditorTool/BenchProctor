# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75157():
    user_id = request.args.get('id', '')
    data = f'{user_id:.200s}'
    int(str(data))
    return jsonify({"result": "success"})
