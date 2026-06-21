# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
import asyncio
from types import SimpleNamespace


def BenchmarkTest40736():
    user_id = request.args.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        return Markup('<div>' + str(data) + '</div>')
    return asyncio.run(_evasion_task())
