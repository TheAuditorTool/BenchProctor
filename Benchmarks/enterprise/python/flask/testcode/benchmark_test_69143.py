# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest69143():
    user_id = request.args.get('id', '')
    exec(str(user_id))
    return jsonify({"result": "success"})
