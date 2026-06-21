# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest64842():
    referer_value = request.headers.get('Referer', '')
    reader = make_reader(referer_value)
    data = reader()
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
