# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def BenchmarkTest28998():
    user_id = request.args.get('id', '')
    data = '{}'.format(user_id)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
