# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13012():
    user_id = request.args.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    eval(str(data))
    return jsonify({"result": "success"})
