# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75688():
    multipart_value = request.form.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
