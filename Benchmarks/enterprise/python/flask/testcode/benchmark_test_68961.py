# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest68961():
    auth_header = request.headers.get('Authorization', '')
    db.users.find({'$where': "this.username == '" + str(auth_header) + "'"})
    return jsonify({"result": "success"})
