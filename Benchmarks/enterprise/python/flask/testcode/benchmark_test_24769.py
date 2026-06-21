# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest24769():
    header_value = request.headers.get('X-Custom-Header', '')
    data = coalesce_blank(header_value)
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return jsonify({'secret': str(secret)}), 200
