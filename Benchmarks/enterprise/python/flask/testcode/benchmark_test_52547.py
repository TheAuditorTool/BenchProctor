# SPDX-License-Identifier: Apache-2.0
import logging
import os
from flask import jsonify


def BenchmarkTest52547():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
