# SPDX-License-Identifier: Apache-2.0
from flask import request
import asyncio
from types import SimpleNamespace


def BenchmarkTest27190():
    auth_header = request.headers.get('Authorization', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return asyncio.run(_evasion_task())
