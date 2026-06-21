# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest09671():
    upload_name = request.files['upload'].filename
    reader = make_reader(upload_name)
    data = reader()
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
