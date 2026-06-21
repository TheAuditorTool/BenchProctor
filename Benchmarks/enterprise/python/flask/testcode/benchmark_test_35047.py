# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import jsonify


def BenchmarkTest35047(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    yaml.safe_load(data)
    return jsonify({"result": "success"})
