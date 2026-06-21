# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest25045():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    reader = make_reader(config_value)
    data = reader()
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
