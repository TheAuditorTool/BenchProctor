# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest02738():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
