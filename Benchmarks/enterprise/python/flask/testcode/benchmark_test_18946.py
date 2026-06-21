# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session


def BenchmarkTest18946():
    multipart_value = request.form.get('multipart_field', '')
    pending = list(str(multipart_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
