# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import asyncio
import urllib.parse


def BenchmarkTest42141():
    field_value = request.form.get('field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
