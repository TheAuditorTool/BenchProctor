# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import time
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest55559(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return jsonify({"result": "success"})
