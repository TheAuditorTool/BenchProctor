# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest37363():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    reader = make_reader(query_array)
    data = reader()
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
