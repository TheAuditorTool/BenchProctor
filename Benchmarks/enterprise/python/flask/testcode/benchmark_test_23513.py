# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest23513():
    referer_value = request.headers.get('Referer', '')
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(referer_value),))
    return jsonify({"result": "success"})
