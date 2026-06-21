# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest71838(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
