# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def BenchmarkTest42454():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
