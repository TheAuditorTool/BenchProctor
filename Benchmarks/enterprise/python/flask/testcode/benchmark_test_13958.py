# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from flask import session


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest13958():
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
