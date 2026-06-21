# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest69086(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
