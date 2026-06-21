# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest70563(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
