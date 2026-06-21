# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest72605():
    raw_body = request.get_data(as_text=True)
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(raw_body),))
    return jsonify({'secret': str(secret)}), 200
