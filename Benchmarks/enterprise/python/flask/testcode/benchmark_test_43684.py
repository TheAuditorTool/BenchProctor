# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify


def BenchmarkTest43684():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(graphql_var)):
        return jsonify({'error': 'invalid input'}), 400
    processed = graphql_var
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
