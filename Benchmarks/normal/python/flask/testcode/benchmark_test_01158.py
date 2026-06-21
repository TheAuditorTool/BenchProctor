# SPDX-License-Identifier: Apache-2.0
import os
from flask import request
from types import SimpleNamespace


def BenchmarkTest01158():
    user_id = request.args.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    checked_path = os.path.normpath(data)
    with open('/var/app/data/' + str(checked_path), 'r') as fh:
        content = fh.read()
    return content
