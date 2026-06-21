# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05866():
    upload_name = request.files['upload'].filename
    data = '%s' % str(upload_name)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
