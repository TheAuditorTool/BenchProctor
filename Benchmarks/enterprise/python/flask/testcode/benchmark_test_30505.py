# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest30505():
    referer_value = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return jsonify({"result": "success"})
