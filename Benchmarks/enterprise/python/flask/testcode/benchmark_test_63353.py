# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest63353():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return jsonify({"result": "success"})
