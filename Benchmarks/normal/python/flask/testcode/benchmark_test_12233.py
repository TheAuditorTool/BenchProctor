# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
import asyncio
from types import SimpleNamespace


def BenchmarkTest12233():
    field_value = request.form.get('field', '')
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        return Markup('<div>' + str(data) + '</div>')
    return asyncio.run(_evasion_task())
