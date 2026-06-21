# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56519():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
