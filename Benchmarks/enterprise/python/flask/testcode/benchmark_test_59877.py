# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest59877():
    header_value = request.headers.get('X-Custom-Header', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
