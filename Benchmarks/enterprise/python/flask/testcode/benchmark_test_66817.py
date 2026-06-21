# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest66817(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    os.unlink('/var/app/data/' + str(data))
    return jsonify({"result": "success"})
