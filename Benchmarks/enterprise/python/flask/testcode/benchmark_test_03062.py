# SPDX-License-Identifier: Apache-2.0
import logging
import os
from flask import jsonify
import json
from app_runtime import db


def BenchmarkTest03062():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return jsonify({"result": "success"})
