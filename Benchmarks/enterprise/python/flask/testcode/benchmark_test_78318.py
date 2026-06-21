# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


def BenchmarkTest78318():
    referer_value = request.headers.get('Referer', '')
    data = ' '.join(str(referer_value).split())
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
