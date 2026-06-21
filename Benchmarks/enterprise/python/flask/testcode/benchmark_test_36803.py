# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest36803():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    reader = make_reader(prop_value)
    data = reader()
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
