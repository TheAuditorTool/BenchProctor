# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest14130():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
