# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import re
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest57846():
    xml_value = request.get_data(as_text=True)
    data = normalise_input(xml_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
