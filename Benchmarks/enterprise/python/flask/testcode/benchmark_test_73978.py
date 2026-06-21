# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest73978():
    multipart_value = request.form.get('multipart_field', '')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(multipart_value),))
    logging.info('request processed')
    return jsonify({"result": "success"})
