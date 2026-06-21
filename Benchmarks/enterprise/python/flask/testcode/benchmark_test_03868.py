# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest03868():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
