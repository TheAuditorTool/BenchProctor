# SPDX-License-Identifier: Apache-2.0
import json
from flask import jsonify


def BenchmarkTest72909(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    json.loads(data)
    return jsonify({"result": "success"})
