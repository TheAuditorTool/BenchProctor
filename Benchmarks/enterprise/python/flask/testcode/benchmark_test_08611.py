# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest08611():
    upload_name = request.files['upload'].filename
    pending = list(str(upload_name).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
