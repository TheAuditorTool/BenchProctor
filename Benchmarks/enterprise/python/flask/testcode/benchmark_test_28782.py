# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest28782():
    referer_value = request.headers.get('Referer', '')
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(referer_value),))
    return jsonify({'secret': str(secret)}), 200
