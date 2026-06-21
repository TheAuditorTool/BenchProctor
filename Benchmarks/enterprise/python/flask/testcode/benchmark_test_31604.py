# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import jsonify


def BenchmarkTest31604(path_param):
    path_value = path_param
    kind = 'json' if str(path_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = path_value
            data = parsed
        case _:
            data = path_value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
