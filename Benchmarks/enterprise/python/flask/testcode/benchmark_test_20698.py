# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest20698(path_param):
    path_value = path_param
    os.chmod('/var/app/data/' + str(path_value), 0o777)
    return jsonify({"result": "success"})
