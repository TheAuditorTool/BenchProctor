# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest30296():
    user_id = request.args.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
