# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import subprocess


def BenchmarkTest30171(path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
