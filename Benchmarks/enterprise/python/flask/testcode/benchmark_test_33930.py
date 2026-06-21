# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import re
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest33930():
    raw_body = request.get_data(as_text=True)
    data = normalise_input(raw_body)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(processed))
    return resp
