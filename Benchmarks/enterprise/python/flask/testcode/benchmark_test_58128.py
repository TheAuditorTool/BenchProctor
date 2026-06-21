# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest58128(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
