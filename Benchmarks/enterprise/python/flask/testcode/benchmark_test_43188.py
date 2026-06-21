# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
import asyncio


def normalise_input(value):
    return value.strip()

def BenchmarkTest43188():
    field_value = request.form.get('field', '')
    data = normalise_input(field_value)
    async def _evasion_task():
        return Markup('<div>' + str(data) + '</div>')
    return asyncio.run(_evasion_task())
