# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest80236():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return jsonify({"result": "success"})
