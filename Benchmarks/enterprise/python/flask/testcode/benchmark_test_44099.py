# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest44099():
    referer_value = request.headers.get('Referer', '')
    with open(os.path.join('/var/app/data', str(referer_value)), 'r') as fh:
        content = fh.read()
    return content
