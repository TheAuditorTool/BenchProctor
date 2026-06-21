# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest43444():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
