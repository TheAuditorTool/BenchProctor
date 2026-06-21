# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest52715():
    auth_header = request.headers.get('Authorization', '')
    reader = make_reader(auth_header)
    data = reader()
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
