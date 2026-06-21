# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest11375():
    header_value = request.headers.get('X-Custom-Header', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return jsonify({"result": "success"})
