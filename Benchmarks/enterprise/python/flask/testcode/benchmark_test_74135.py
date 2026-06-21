# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import jsonify


def BenchmarkTest74135(path_param):
    path_value = path_param
    data = f'{path_value}'
    yaml.safe_load(data)
    return jsonify({"result": "success"})
