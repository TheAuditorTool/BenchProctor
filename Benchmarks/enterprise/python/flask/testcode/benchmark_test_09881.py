# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest09881():
    referer_value = request.headers.get('Referer', '')
    reader = make_reader(referer_value)
    data = reader()
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
