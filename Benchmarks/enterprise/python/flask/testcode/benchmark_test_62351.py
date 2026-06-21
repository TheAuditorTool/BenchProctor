# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest62351(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    os.unlink('/var/app/data/' + str(data))
    return jsonify({"result": "success"})
