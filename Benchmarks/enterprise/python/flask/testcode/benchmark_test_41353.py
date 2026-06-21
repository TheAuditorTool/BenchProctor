# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest41353():
    header_value = request.headers.get('X-Custom-Header', '')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(header_value),))
    return jsonify({"result": "success"})
