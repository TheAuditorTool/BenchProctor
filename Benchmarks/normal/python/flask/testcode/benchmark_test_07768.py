# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import json


def BenchmarkTest07768(path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    json.loads(data)
    return jsonify({"result": "success"})
