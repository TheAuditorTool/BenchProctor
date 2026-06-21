# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59437():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % str(multipart_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    trusted_claim = str(processed)
    return jsonify({'trusted': trusted_claim}), 200
