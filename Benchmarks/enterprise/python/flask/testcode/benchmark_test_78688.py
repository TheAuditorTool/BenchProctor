# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest78688():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return jsonify({"result": "success"})
