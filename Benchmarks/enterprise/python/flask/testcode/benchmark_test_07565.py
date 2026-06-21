# SPDX-License-Identifier: Apache-2.0
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest07565():
    raw_body = request.get_data(as_text=True)
    reader = make_reader(raw_body)
    data = reader()
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
