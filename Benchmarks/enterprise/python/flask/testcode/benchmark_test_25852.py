# SPDX-License-Identifier: Apache-2.0
import subprocess
import os
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest25852():
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
