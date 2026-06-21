# SPDX-License-Identifier: Apache-2.0
import os
from flask import request
from types import SimpleNamespace


def BenchmarkTest73021():
    host_value = request.headers.get('Host', '')
    ns = SimpleNamespace(payload=host_value)
    data = getattr(ns, 'payload')
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
