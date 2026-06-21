# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest63538():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return jsonify({"result": "success"})
