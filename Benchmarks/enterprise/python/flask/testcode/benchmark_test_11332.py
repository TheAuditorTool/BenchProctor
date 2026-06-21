# SPDX-License-Identifier: Apache-2.0
import re
import json
from flask import request, jsonify


def BenchmarkTest11332():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
