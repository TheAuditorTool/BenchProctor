# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest42062():
    ua_value = request.headers.get('User-Agent', '')
    data = ' '.join(str(ua_value).split())
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return jsonify({"result": "success"})
