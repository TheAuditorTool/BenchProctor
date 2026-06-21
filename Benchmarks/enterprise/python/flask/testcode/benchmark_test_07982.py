# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07982():
    user_id = request.args.get('id', '')
    data = f'{user_id}'
    eval(str(data))
    return jsonify({"result": "success"})
