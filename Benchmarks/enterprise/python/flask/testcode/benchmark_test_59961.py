# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def BenchmarkTest59961():
    referer_value = request.headers.get('Referer', '')
    data = str(referer_value).replace('\x00', '')
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
