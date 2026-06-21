# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest69000():
    user_id = request.args.get('id', '')
    data = (lambda v: v.strip())(user_id)
    if session.get('role') != 'admin':
        return jsonify({'error': 'forbidden'}), 403
    session['data'] = str(data)
    return jsonify({"result": "success"})
