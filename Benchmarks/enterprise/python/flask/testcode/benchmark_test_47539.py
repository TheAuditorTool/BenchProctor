# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest47539():
    ua_value = request.headers.get('User-Agent', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(ua_value)
    data = collected
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
