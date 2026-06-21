# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest63274():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % str(header_value)
    if session.get('role') != 'admin':
        return jsonify({'error': 'forbidden'}), 403
    session['data'] = str(data)
    return jsonify({"result": "success"})
