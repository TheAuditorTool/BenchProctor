# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77205():
    user_id = request.args.get('id', '')
    if not str(user_id).isdigit():
        raise Exception('error: ' + str(user_id))
    return jsonify({"result": "success"})
