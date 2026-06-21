# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def BenchmarkTest11914():
    referer_value = request.headers.get('Referer', '')
    checked_path = os.path.join('/var/app/data', os.path.basename(referer_value))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
