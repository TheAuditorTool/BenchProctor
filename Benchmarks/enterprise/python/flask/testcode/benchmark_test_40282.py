# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def relay_value(value):
    return value

def BenchmarkTest40282():
    origin_value = request.headers.get('Origin', '')
    data = relay_value(origin_value)
    processed = data[:64]
    link_path = os.path.join('/var/app/data', str(processed))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
