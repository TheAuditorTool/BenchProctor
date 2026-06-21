# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest77136():
    header_value = request.headers.get('X-Custom-Header', '')
    reader = make_reader(header_value)
    data = reader()
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
