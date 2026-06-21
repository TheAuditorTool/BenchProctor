# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
import asyncio


def normalise_input(value):
    return value.strip()

def BenchmarkTest14502():
    auth_header = request.headers.get('Authorization', '')
    data = normalise_input(auth_header)
    async def _evasion_task():
        return Markup('<div>' + str(data) + '</div>')
    return asyncio.run(_evasion_task())
