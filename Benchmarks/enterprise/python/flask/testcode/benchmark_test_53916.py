# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import os
from flask import jsonify


def BenchmarkTest53916():
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
