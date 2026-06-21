# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest37041(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
