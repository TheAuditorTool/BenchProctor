# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest04076(path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    exec(str(data))
    return jsonify({"result": "success"})
