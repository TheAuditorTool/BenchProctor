# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest76368():
    upload_name = request.files['upload'].filename
    prefix = ''
    data = prefix + str(upload_name)
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return jsonify({"result": "success"})
