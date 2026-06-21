# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05126():
    upload_name = request.files['upload'].filename
    data = '%s' % (upload_name,)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
