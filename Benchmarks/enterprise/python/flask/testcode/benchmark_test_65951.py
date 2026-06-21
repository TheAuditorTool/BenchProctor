# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest65951():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return jsonify({"result": "success"})
