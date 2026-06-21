# SPDX-License-Identifier: Apache-2.0
import logging
import os
from flask import jsonify


def BenchmarkTest61748():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
