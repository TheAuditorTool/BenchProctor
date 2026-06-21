# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest03705():
    user_id = request.args.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
