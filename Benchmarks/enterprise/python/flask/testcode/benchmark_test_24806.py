# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest24806():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
