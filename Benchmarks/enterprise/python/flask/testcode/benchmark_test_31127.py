# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest31127():
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    return jsonify({'error': 'An internal error occurred'}), 500
