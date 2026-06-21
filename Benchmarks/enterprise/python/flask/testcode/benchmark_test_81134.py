# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest81134():
    upload_name = request.files['upload'].filename
    data = str(upload_name).replace('\x00', '')
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
