# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest53098():
    user_id = request.args.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return jsonify({"result": "success"})
