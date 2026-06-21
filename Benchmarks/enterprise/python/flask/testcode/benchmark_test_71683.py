# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest71683():
    user_id = request.args.get('id', '')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(user_id),))
    logging.info('request processed')
    return jsonify({"result": "success"})
