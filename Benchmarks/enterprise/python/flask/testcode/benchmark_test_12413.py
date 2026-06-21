# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12413():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    trusted_claim = str(processed)
    return jsonify({'trusted': trusted_claim}), 200
