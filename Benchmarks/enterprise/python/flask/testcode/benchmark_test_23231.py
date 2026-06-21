# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest23231(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
