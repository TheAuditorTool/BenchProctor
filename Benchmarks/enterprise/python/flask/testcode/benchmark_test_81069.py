# SPDX-License-Identifier: Apache-2.0
import os
from urllib.parse import unquote
from flask import request


def BenchmarkTest81069():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
