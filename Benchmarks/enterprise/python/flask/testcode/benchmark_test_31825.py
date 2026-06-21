# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31825():
    user_id = request.args.get('id', '')
    data = f'{user_id}'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    trusted_claim = str(processed)
    return jsonify({'trusted': trusted_claim}), 200
