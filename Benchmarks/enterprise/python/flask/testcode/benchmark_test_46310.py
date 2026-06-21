# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def to_text(value):
    return str(value).strip()

def BenchmarkTest46310():
    raw_body = request.get_data(as_text=True)
    data = to_text(raw_body)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
