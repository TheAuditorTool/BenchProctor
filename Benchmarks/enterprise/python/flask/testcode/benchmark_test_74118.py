# SPDX-License-Identifier: Apache-2.0
import os
from flask import request
from types import SimpleNamespace


def BenchmarkTest74118():
    referer_value = request.headers.get('Referer', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
