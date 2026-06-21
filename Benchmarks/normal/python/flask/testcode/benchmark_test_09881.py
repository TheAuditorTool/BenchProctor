# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest09881():
    host_value = request.headers.get('Host', '')
    reader = make_reader(host_value)
    data = reader()
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
