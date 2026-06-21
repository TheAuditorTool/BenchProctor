# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import jsonify
import json


def BenchmarkTest77251(path_param):
    path_value = path_param
    data = unquote(path_value)
    json.loads(data)
    return jsonify({"result": "success"})
