# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
import asyncio
from types import SimpleNamespace


def BenchmarkTest69173():
    cookie_value = request.cookies.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        return Markup('<div>' + str(data) + '</div>')
    return asyncio.run(_evasion_task())
