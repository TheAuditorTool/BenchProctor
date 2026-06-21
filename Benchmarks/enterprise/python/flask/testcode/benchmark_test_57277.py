# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest57277():
    referer_value = request.headers.get('Referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return jsonify({"result": "success"})
