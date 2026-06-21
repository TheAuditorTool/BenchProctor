# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61457():
    upload_name = request.files['upload'].filename
    kind = 'json' if str(upload_name).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = upload_name
            data = parsed
        case _:
            data = upload_name
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
