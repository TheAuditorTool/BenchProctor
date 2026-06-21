# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest45862(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
