# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest22686():
    user_id = request.args.get('id', '')
    data = '%s' % (user_id,)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
