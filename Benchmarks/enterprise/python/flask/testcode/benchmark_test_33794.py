# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from flask import session


def BenchmarkTest33794():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
