# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest21038(path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
