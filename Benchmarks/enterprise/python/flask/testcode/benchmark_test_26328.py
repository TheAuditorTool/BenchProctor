# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
import os


def BenchmarkTest26328():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    parts = str(dotenv_value).split(',')
    data = ','.join(parts)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
