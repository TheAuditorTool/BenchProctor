# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest62154():
    upload_name = request.files['upload'].filename
    return jsonify({'error': str(upload_name), 'stack': repr(locals())}), 500
