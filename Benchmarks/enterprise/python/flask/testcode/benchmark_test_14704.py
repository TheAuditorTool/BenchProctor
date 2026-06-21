# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest14704():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
