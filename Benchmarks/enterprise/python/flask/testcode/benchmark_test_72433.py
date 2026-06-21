# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest72433():
    upload_name = request.files['upload'].filename
    data = coalesce_blank(upload_name)
    return jsonify({'error': 'An internal error occurred'}), 500
