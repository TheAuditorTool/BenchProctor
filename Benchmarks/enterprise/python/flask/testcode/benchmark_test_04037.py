# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04037():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body:.200s}'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
