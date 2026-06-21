# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest46985():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
