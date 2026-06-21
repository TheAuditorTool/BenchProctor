# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest55593():
    user_id = request.args.get('id', '')
    data = f'{user_id:.200s}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
