# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest57684(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
