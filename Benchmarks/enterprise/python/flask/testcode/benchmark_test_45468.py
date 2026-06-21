# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest45468():
    upload_name = request.files['upload'].filename
    if upload_name:
        data = upload_name
    else:
        data = ''
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
