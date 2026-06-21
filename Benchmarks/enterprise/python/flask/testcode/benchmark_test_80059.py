# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest80059():
    xml_value = request.get_data(as_text=True)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(xml_value),))
    logging.info('request processed')
    return jsonify({"result": "success"})
