# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
import os


def BenchmarkTest21952():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(dotenv_value), max_age=86400)
    return resp
