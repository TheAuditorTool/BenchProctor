# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10682():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % str(multipart_value)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
