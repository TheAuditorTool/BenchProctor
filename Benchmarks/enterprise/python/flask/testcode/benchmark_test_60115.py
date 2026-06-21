# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest60115(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
