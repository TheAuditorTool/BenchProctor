# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest74843():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value:.200s}'
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
