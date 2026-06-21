# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest36972(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
