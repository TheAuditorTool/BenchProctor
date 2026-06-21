# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest52045():
    ua_value = request.headers.get('User-Agent', '')
    data = coalesce_blank(ua_value)
    processed = data[:64]
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return jsonify({"result": "success"})
