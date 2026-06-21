# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest16909():
    user_id = request.args.get('id', '')
    data = str(user_id).replace('\x00', '')
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return jsonify({'secret': str(secret)}), 200
