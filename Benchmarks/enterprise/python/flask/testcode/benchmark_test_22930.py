# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22930():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value:.200s}'
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
