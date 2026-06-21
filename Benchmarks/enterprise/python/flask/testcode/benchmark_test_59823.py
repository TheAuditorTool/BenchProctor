# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify


def BenchmarkTest59823(path_param):
    path_value = path_param
    pending = list(str(path_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
