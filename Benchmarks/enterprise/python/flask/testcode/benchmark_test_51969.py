# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest51969():
    origin_value = request.headers.get('Origin', '')
    link_path = os.path.join('/var/app/data', str(origin_value))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
