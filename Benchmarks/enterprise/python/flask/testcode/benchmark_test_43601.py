# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest43601():
    env_value = os.environ.get('USER_INPUT', '')
    prefix = ''
    data = prefix + str(env_value)
    os.unlink('/var/app/data/' + str(data))
    return jsonify({"result": "success"})
