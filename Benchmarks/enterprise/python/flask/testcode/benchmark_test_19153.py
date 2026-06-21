# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest19153():
    multipart_value = request.form.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
