# SPDX-License-Identifier: Apache-2.0
import logging
import os
from flask import jsonify


def BenchmarkTest00301():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
