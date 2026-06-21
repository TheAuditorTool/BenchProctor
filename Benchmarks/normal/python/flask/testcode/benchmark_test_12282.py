# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest12282(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return jsonify({"result": "success"})
