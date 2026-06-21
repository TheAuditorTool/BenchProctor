# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest12718():
    auth_header = request.headers.get('Authorization', '')
    pending = list(str(auth_header).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return jsonify({"result": "success"})
