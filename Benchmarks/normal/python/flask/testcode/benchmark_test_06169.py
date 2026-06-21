# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest06169():
    upload_name = request.files['upload'].filename
    data = coalesce_blank(upload_name)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
