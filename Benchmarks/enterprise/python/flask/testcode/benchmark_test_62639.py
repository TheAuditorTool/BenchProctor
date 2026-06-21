# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify


def BenchmarkTest62639(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
