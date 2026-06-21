# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest38587(path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
