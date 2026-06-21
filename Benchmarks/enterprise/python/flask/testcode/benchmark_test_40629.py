# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import jsonify


def BenchmarkTest40629(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    yaml.safe_load(data)
    return jsonify({"result": "success"})
