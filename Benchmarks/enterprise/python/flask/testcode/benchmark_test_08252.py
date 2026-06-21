# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest08252():
    auth_header = request.headers.get('Authorization', '')
    data = str(auth_header).replace('\x00', '')
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return jsonify({"result": "success"})
