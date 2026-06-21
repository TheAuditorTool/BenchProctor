# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest52727():
    multipart_value = request.form.get('multipart_field', '')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(multipart_value))
    return resp
