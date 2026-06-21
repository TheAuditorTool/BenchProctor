# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest48635():
    xml_value = request.get_data(as_text=True)
    reader = make_reader(xml_value)
    data = reader()
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
