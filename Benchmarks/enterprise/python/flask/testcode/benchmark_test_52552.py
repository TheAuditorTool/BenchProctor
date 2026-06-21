# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import jsonify


def BenchmarkTest52552(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
