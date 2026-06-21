# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify


def BenchmarkTest65245(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
