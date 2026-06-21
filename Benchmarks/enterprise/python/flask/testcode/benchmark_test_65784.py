# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest65784():
    multipart_value = request.form.get('multipart_field', '')
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(multipart_value)}
