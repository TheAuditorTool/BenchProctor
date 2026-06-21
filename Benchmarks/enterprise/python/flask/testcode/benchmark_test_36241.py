# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest36241():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return jsonify({"result": "success"})
