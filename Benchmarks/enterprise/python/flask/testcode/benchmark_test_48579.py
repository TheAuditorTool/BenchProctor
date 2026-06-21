# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
import os


def BenchmarkTest48579():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = dotenv_value if dotenv_value else 'default'
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
