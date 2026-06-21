# SPDX-License-Identifier: Apache-2.0
import logging
import os
from flask import jsonify
import json


def BenchmarkTest42492():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
