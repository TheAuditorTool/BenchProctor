# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest60159():
    field_value = request.form.get('field', '')
    reader = make_reader(field_value)
    data = reader()
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
