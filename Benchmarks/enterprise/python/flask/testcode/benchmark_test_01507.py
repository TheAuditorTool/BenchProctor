# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01507():
    upload_name = request.files['upload'].filename
    data = upload_name if upload_name else 'default'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
