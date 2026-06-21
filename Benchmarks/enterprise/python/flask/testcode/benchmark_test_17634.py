# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest17634():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header}'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    exec(str(processed))
    return jsonify({"result": "success"})
