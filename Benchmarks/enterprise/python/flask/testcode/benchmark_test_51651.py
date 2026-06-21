# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
from app_runtime import db


def ensure_str(value):
    return str(value)

def BenchmarkTest51651():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = ensure_str(graphql_var)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return jsonify({"result": "success"})
