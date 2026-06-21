# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
import os


def BenchmarkTest70187():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = str(dotenv_value).replace('\x00', '')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
