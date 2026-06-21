# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest08456():
    host_value = request.headers.get('Host', '')
    reader = make_reader(host_value)
    data = reader()
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
