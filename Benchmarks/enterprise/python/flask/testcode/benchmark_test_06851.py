# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest06851():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
