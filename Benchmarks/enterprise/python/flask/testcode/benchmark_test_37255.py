# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import jsonify


def BenchmarkTest37255(path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
