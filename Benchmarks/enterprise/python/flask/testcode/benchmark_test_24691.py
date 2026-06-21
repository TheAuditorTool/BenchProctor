# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest24691(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
