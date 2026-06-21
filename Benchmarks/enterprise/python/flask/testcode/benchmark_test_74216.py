# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest74216():
    xml_value = request.get_data(as_text=True)
    reader = make_reader(xml_value)
    data = reader()
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
