# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time
from types import SimpleNamespace


def BenchmarkTest16973():
    user_id = request.args.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        eval(str(data))
    return jsonify({"result": "success"})
