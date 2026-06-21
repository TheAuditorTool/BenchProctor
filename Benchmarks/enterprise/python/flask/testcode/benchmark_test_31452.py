# SPDX-License-Identifier: Apache-2.0
from flask import request
import os
import asyncio
from types import SimpleNamespace


def BenchmarkTest31452():
    host_value = request.headers.get('Host', '')
    ns = SimpleNamespace(payload=host_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
            content = fh.read()
        return content
    return asyncio.run(_evasion_task())
