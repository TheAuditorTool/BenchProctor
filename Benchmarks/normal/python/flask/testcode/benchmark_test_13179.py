# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest13179():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
