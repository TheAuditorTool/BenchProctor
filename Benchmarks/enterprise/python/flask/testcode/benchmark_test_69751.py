# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def coalesce_blank(value):
    return value or ''

def BenchmarkTest69751():
    raw_body = request.get_data(as_text=True)
    data = coalesce_blank(raw_body)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
