# SPDX-License-Identifier: Apache-2.0
import yaml
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest10697(path_param):
    path_value = path_param
    data = unquote(path_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
