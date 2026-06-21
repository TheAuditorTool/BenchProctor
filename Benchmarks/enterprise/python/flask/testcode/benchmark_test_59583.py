# SPDX-License-Identifier: Apache-2.0
from flask import session
import os
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest59583():
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    session['data'] = str(data)
    return jsonify({"result": "success"})
