# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest10413(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
