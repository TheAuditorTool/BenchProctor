# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest09230(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    os.unlink('/var/app/data/' + str(data))
    return jsonify({"result": "success"})
