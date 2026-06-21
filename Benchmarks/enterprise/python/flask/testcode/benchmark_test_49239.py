# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest49239():
    header_value = request.headers.get('X-Custom-Header', '')
    kind = 'json' if str(header_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = header_value
            data = parsed
        case _:
            data = header_value
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
