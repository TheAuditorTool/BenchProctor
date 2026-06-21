# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest09916():
    raw_body = request.get_data(as_text=True)
    data = '{}'.format(raw_body)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
