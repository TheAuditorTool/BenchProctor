# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest13214():
    upload_name = request.files['upload'].filename
    reader = make_reader(upload_name)
    data = reader()
    return jsonify({'error': 'An internal error occurred'}), 500
