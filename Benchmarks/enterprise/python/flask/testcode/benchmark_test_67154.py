# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest67154():
    user_id = request.args.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
