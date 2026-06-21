# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest61560(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    eval(str(processed))
    return jsonify({"result": "success"})
