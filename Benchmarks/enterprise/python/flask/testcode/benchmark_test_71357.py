# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest71357(path_param):
    path_value = path_param
    kind = 'json' if str(path_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = path_value
            data = parsed
        case _:
            data = path_value
    os.seteuid(65534)
    return jsonify({"result": "success"})
