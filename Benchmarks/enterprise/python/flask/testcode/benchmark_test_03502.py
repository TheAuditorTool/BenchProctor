# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest03502():
    ua_value = request.headers.get('User-Agent', '')
    data = ' '.join(str(ua_value).split())
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
