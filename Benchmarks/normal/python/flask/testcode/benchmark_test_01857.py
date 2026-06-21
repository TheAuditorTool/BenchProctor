# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest01857():
    user_id = request.args.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
