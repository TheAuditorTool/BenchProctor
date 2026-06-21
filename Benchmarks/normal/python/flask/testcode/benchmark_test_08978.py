# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08978():
    raw_body = request.get_data(as_text=True)
    data = '%s' % str(raw_body)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    trusted_claim = str(processed)
    return jsonify({'trusted': trusted_claim}), 200
