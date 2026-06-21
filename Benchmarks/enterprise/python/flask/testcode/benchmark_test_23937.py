# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest23937():
    raw_body = request.get_data(as_text=True)
    data = '%s' % str(raw_body)
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
