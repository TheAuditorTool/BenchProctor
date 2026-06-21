# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest67855():
    multipart_value = request.form.get('multipart_field', '')
    data, _sep, _rest = str(multipart_value).partition('\x00')
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
