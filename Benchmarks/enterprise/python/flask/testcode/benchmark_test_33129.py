# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import json


def BenchmarkTest33129(path_param):
    path_value = path_param
    pending = list(str(path_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    json.loads(data)
    return jsonify({"result": "success"})
