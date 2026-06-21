# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest46411():
    field_value = request.form.get('field', '')
    data = '%s' % (field_value,)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
