# SPDX-License-Identifier: Apache-2.0
import threading
import os
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest13263():
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
