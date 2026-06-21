# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
import os


def normalise_input(value):
    return value.strip()

def BenchmarkTest69672():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = normalise_input(dotenv_value)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
