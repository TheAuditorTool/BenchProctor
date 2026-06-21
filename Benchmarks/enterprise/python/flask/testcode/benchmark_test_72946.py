# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72946():
    upload_name = request.files['upload'].filename
    data = '%s' % str(upload_name)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
