# SPDX-License-Identifier: Apache-2.0
import threading
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest27725(path_param):
    path_value = path_param
    data = unquote(path_value)
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
