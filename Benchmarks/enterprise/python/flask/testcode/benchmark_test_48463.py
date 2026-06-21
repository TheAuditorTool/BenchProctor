# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest48463():
    ua_value = request.headers.get('User-Agent', '')
    reader = make_reader(ua_value)
    data = reader()
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
