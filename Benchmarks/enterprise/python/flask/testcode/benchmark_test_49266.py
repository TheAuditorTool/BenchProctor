# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest49266():
    multipart_value = request.form.get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ','.join(parts)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
