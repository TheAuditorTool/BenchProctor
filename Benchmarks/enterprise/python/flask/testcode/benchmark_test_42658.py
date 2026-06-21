# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest42658():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return jsonify({"result": "success"})
