# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest12000():
    raw_body = request.get_data(as_text=True)
    with open('/var/app/data/' + str(raw_body), 'r') as fh:
        content = fh.read()
    return content
