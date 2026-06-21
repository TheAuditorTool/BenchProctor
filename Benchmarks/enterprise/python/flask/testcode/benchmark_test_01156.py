# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest01156():
    field_value = request.form.get('field', '')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(field_value))
    return resp
