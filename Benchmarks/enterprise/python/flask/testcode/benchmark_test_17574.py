# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest17574():
    multipart_value = request.form.get('multipart_field', '')
    ns = SimpleNamespace(payload=multipart_value)
    data = getattr(ns, 'payload')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
