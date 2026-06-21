# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest49479(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    int(str(data))
    return jsonify({"result": "success"})
