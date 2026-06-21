# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import jsonify


def BenchmarkTest07217(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    yaml.safe_load(data)
    return jsonify({"result": "success"})
