# SPDX-License-Identifier: Apache-2.0
import logging
from urllib.parse import unquote
from flask import jsonify
from app_runtime import db


def BenchmarkTest10935(path_param):
    path_value = path_param
    data = unquote(path_value)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return jsonify({"result": "success"})
