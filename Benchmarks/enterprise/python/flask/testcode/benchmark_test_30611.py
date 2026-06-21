# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import jsonify
import json


def BenchmarkTest30611(path_param):
    path_value = path_param
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
