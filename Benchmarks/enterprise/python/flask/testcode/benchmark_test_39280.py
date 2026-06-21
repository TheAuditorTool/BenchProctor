# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39280():
    raw_body = request.get_data(as_text=True)
    data = '%s' % (raw_body,)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
