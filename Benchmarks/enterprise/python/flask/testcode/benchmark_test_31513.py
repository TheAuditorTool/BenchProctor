# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
import os


request_state: dict[str, str] = {}

def BenchmarkTest31513():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    request_state['last_input'] = dotenv_value
    data = request_state['last_input']
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
