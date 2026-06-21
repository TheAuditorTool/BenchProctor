# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest13050():
    ua_value = request.headers.get('User-Agent', '')
    reader = make_reader(ua_value)
    data = reader()
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
