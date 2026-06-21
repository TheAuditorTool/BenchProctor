# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest24976():
    raw_body = request.get_data(as_text=True)
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(raw_body),))
    return jsonify({"result": "success"})
