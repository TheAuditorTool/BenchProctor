# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32488():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % str(multipart_value)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
