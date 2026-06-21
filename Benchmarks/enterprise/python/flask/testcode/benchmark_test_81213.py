# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify


def BenchmarkTest81213(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
