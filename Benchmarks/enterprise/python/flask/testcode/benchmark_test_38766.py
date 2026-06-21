# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest38766():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return jsonify({"result": "success"})
