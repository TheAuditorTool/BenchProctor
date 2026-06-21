# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest57672():
    raw_body = request.get_data(as_text=True)
    data = normalise_input(raw_body)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
