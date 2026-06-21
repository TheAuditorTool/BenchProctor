# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest21635():
    cookie_value = request.cookies.get('session_token', '')
    reader = make_reader(cookie_value)
    data = reader()
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
