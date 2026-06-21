# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00736():
    multipart_value = request.form.get('multipart_field', '')
    pending = list(str(multipart_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
