# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest30330():
    cookie_value = request.cookies.get('session_token', '')
    reader = make_reader(cookie_value)
    data = reader()
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
