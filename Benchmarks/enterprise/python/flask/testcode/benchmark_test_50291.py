# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest50291():
    multipart_value = request.form.get('multipart_field', '')
    kind = 'json' if str(multipart_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = multipart_value
            data = parsed
        case _:
            data = multipart_value
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
