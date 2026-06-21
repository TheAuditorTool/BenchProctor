# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest77302():
    multipart_value = request.form.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
