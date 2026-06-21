# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest44615():
    user_id = request.args.get('id', '')
    link_path = os.path.join('/var/app/data', str(user_id))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
