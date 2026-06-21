# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest51395(path_param):
    path_value = path_param
    data = default_blank(path_value)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
