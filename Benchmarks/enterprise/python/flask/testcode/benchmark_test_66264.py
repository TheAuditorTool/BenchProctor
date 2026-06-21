# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import os
from flask import jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest66264():
    env_value = os.environ.get('USER_INPUT', '')
    data = normalise_input(env_value)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
