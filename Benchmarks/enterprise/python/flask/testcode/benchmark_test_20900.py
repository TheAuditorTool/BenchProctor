# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest20900():
    upload_name = request.files['upload'].filename
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(upload_name),))
    return jsonify({'secret': str(secret)}), 200
