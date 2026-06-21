# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest05027():
    raw_body = request.get_data(as_text=True)
    reader = make_reader(raw_body)
    data = reader()
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
