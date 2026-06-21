# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35306():
    upload_name = request.files['upload'].filename
    pending = list(str(upload_name).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
