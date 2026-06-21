# SPDX-License-Identifier: Apache-2.0
import logging
import os
from flask import jsonify


def BenchmarkTest02444():
    env_value = os.environ.get('USER_INPUT', '')
    logging.info('User action: ' + str(env_value))
    return jsonify({"result": "success"})
