# SPDX-License-Identifier: Apache-2.0
import logging
import os
from flask import jsonify
from app_runtime import db


def BenchmarkTest15624():
    env_value = os.environ.get('USER_INPUT', '')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(env_value),))
    logging.info('audit actor=%s action=revoke_sessions', str(env_value))
    return jsonify({"result": "success"})
