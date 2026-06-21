# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest72614(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return jsonify({"result": "success"})
