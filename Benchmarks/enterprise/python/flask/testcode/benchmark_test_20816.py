# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest20816():
    referer_value = request.headers.get('Referer', '')
    data = str(referer_value).replace('\x00', '')
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return jsonify({"result": "success"})
