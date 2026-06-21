# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest35928():
    origin_value = request.headers.get('Origin', '')
    data = normalise_input(origin_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
