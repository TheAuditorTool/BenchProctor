# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest63066():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    os.remove(str(data))
    return jsonify({"result": "success"})
