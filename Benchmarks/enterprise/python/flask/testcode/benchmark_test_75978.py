# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import jsonify
import json


def BenchmarkTest75978(path_param):
    path_value = path_param
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
