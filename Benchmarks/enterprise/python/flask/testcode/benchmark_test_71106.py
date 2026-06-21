# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
import asyncio


def BenchmarkTest71106():
    upload_name = request.files['upload'].filename
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(upload_name)
    data = collected
    async def _evasion_task():
        return Markup('<div>' + str(data) + '</div>')
    return asyncio.run(_evasion_task())
