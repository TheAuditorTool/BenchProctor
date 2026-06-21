# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest04805(path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    int(str(data))
    return jsonify({"result": "success"})
