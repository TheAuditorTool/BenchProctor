# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00225(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
