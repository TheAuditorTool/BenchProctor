# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest76152():
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
