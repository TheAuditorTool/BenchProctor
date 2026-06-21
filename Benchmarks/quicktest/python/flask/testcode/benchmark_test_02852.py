# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest02852():
    raw_body = request.get_data(as_text=True)
    data = (lambda v: v.strip())(raw_body)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
