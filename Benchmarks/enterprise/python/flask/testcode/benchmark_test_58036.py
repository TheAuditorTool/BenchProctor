# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest58036():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
