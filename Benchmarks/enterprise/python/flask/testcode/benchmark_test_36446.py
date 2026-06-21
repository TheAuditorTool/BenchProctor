# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest36446():
    multipart_value = request.form.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
