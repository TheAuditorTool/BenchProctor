# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest29086():
    user_id = request.args.get('id', '')
    data = relay_value(user_id)
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
