# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest21298(path_param):
    path_value = path_param
    data = f'{path_value}'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    eval(str(processed))
    return jsonify({"result": "success"})
