# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest47783():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
