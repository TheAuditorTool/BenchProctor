# SPDX-License-Identifier: Apache-2.0
from flask import request
import os
from types import SimpleNamespace


def BenchmarkTest44277():
    user_id = request.args.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    def _primary():
        link_path = os.path.join('/var/app/data', str(data))
        target = os.readlink(link_path)
        with open(target, 'r') as fh:
            content = fh.read()
        return content
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
