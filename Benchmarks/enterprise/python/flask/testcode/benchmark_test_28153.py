# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest28153(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return jsonify({"result": "success"})
