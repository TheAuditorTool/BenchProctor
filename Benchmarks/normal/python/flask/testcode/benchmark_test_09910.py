# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest09910():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    ns = SimpleNamespace(payload=forwarded_ip)
    data = getattr(ns, 'payload')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return jsonify({"result": "success"})
