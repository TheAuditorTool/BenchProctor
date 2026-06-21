# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest57844(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
