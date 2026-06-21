# SPDX-License-Identifier: Apache-2.0
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest01539():
    referer_value = request.headers.get('Referer', '')
    reader = make_reader(referer_value)
    data = reader()
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
