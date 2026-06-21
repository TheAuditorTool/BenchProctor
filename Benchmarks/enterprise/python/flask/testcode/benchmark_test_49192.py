# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest49192():
    raw_body = request.get_data(as_text=True)
    db.execute('SELECT * FROM users WHERE id = ' + str(raw_body))
    return jsonify({"result": "success"})
