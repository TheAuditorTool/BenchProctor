# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22244():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % (multipart_value,)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
