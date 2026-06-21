# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest02429():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    reader = make_reader(forwarded_ip)
    data = reader()
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
