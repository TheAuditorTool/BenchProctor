# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest00777():
    host_value = request.headers.get('Host', '')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(host_value),))
    return jsonify({"result": "success"})
