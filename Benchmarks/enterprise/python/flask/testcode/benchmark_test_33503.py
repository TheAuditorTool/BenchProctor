# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest33503():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return jsonify({"result": "success"})
