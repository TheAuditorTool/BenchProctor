# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest12206():
    user_id = request.args.get('id', '')
    data = ' '.join(str(user_id).split())
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
