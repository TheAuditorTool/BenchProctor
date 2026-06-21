# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest39353():
    user_id = request.args.get('id', '')
    with open(os.path.join('/var/app/data', str(user_id)), 'r') as fh:
        content = fh.read()
    return content
