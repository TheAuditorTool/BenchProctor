# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest22214():
    raw_body = request.get_data(as_text=True)
    data = (lambda v: v.strip())(raw_body)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
