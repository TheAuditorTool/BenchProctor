# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest07573():
    multipart_value = request.form.get('multipart_field', '')
    data = coalesce_blank(multipart_value)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return jsonify({"result": "success"})
