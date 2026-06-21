# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest70478():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % str(referer_value)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return jsonify({"result": "success"})
