# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest06270():
    cookie_value = request.cookies.get('session_token', '')
    data = normalise_input(cookie_value)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return jsonify({"result": "success"})
