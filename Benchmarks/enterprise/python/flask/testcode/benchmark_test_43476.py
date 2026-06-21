# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest43476(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
