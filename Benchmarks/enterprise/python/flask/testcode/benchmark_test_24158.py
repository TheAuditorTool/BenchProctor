# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest24158():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
