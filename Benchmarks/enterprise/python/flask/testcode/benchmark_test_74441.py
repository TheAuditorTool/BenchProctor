# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def BenchmarkTest74441():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
