# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest47315():
    upload_name = request.files['upload'].filename
    data = default_blank(upload_name)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
