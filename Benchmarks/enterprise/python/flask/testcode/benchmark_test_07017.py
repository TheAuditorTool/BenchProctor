# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest07017():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return jsonify({'secret': str(secret)}), 200
