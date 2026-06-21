# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest32121():
    raw_body = request.get_data(as_text=True)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(raw_body),))
    return jsonify({"result": "success"})
