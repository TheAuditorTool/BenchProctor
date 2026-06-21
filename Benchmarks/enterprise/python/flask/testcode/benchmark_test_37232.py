# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest37232(path_param):
    path_value = path_param
    data = f'{path_value}'
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return jsonify({"result": "success"})
