# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest75136():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
