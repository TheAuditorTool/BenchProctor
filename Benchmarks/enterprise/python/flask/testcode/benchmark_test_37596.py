# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest37596(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
