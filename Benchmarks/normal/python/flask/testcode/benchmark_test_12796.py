# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest12796(path_param):
    path_value = path_param
    with open('/var/uploads/' + str(path_value), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
