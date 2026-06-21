# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest22277():
    referer_value = request.headers.get('Referer', '')
    reader = make_reader(referer_value)
    data = reader()
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})
