# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest25930():
    referer_value = request.headers.get('Referer', '')
    data = relay_value(referer_value)
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return jsonify({"result": "success"})
