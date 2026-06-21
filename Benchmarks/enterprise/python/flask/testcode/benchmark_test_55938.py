# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest55938():
    user_id = request.args.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
