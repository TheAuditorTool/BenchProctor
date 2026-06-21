# SPDX-License-Identifier: Apache-2.0
import secrets
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest41836():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
