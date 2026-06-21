# SPDX-License-Identifier: Apache-2.0
import os
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest25263(path_param):
    path_value = path_param
    data = unquote(path_value)
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return jsonify({"result": "success"})
