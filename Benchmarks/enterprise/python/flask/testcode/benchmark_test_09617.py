# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest09617():
    referer_value = request.headers.get('Referer', '')
    data = (lambda v: v.strip())(referer_value)
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return jsonify({"result": "success"})
