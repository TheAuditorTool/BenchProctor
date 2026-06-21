# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest78133():
    multipart_value = request.form.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
