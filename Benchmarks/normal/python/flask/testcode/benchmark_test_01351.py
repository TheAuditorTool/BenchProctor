# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest01351(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
