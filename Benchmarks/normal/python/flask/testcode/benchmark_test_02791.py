# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest02791():
    raw_body = request.get_data(as_text=True)
    data = coalesce_blank(raw_body)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
