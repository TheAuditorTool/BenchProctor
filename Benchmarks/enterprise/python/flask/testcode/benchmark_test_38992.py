# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest38992():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
