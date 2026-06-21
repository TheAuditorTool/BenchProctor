# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest68799():
    multipart_value = request.form.get('multipart_field', '')
    pending = list(str(multipart_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
