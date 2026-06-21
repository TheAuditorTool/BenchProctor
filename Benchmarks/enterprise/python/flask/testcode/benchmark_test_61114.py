# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify


def BenchmarkTest61114(path_param):
    path_value = path_param
    globals()['counter'] = int(path_value)
    return jsonify({"result": "success"})
