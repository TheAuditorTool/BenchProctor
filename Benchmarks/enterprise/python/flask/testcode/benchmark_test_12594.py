# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest12594(path_param):
    path_value = path_param
    processed = 'true' if str(path_value).lower() in ('true', '1', 'yes', 'on') else 'false'
    eval(str(processed))
    return jsonify({"result": "success"})
