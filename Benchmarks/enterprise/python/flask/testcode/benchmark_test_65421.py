# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest65421():
    field_value = request.form.get('field', '')
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(field_value).replace('\r', '').replace('\n', ''))
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
