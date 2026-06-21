# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest45200():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = graphql_var if graphql_var else 'default'
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return jsonify({"result": "success"})
