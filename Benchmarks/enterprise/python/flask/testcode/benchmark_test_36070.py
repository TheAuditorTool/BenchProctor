# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest36070():
    upload_name = request.files['upload'].filename
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(upload_name),))
    logging.info('request processed')
    return jsonify({"result": "success"})
