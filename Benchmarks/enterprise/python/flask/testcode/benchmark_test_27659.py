# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest27659():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % (multipart_value,)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
