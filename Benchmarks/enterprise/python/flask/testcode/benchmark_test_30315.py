# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest30315():
    user_id = request.args.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
