# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
from flask import session


def BenchmarkTest17014():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
