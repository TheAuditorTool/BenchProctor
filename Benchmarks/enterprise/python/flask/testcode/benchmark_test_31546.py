# SPDX-License-Identifier: Apache-2.0
import logging
import os
from flask import jsonify
from app_runtime import db


def BenchmarkTest31546():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return jsonify({"result": "success"})
