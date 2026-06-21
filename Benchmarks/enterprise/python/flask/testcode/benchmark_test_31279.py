# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31279():
    multipart_value = request.form.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    trusted_claim = str(processed)
    return jsonify({'trusted': trusted_claim}), 200
