# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest40028():
    field_value = request.form.get('field', '')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(field_value),))
    logging.info('request processed')
    return jsonify({"result": "success"})
