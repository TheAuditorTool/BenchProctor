# SPDX-License-Identifier: Apache-2.0
import subprocess
import os
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest62846():
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return jsonify({"result": "success"})
