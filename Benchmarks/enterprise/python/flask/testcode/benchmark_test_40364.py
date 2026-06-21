# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest40364():
    xml_value = request.get_data(as_text=True)
    reader = make_reader(xml_value)
    data = reader()
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
