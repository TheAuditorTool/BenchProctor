# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest22217(path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    os.remove(str(data))
    return jsonify({"result": "success"})
