# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest55790():
    referer_value = request.headers.get('Referer', '')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(referer_value),))
    return jsonify({"result": "success"})
