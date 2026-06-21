# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest08124():
    user_id = request.args.get('id', '')
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(user_id),))
    return jsonify({'secret': str(secret)}), 200
