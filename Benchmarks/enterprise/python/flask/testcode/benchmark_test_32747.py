# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest32747():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    reader = make_reader(dotenv_value)
    data = reader()
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
