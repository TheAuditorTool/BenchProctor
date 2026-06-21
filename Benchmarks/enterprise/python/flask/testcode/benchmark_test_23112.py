# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest23112():
    user_id = request.args.get('id', '')
    data = ' '.join(str(user_id).split())
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
