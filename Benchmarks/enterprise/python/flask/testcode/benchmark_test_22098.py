# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import jsonify


def BenchmarkTest22098(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    yaml.safe_load(data)
    return jsonify({"result": "success"})
