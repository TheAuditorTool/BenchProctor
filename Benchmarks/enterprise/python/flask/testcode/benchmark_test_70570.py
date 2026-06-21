# SPDX-License-Identifier: Apache-2.0
import logging
import os
from flask import jsonify


def BenchmarkTest70570():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
