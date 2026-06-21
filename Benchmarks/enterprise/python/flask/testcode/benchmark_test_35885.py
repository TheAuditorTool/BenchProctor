# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest35885():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(json_value).replace('\r', '').replace('\n', ''))
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
