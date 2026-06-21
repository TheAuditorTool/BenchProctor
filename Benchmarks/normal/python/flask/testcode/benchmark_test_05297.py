# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest05297():
    host_value = request.headers.get('Host', '')
    reader = make_reader(host_value)
    data = reader()
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
