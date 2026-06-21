# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest54127():
    header_value = request.headers.get('X-Custom-Header', '')
    pending = list(str(header_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return jsonify({"result": "success"})
