# SPDX-License-Identifier: Apache-2.0
import logging
import json
from flask import request, jsonify


def BenchmarkTest16306():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
