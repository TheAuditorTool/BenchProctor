# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest62481():
    user_id = request.args.get('id', '')
    data = '%s' % str(user_id)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
