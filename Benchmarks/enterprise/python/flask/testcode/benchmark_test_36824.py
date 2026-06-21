# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from dataclasses import dataclass
from flask import jsonify
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest36824():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = FormData(payload=dotenv_value).payload
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
