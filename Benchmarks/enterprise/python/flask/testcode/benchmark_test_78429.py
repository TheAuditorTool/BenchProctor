# SPDX-License-Identifier: Apache-2.0
import logging
import os
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest78429():
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
