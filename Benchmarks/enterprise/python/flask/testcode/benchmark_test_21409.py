# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest21409(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
