# SPDX-License-Identifier: Apache-2.0
import logging
import os
from flask import jsonify
from app_runtime import db


def BenchmarkTest68591():
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return jsonify({"result": "success"})
