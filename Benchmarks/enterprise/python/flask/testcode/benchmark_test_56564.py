# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import asyncio
import urllib.parse


def BenchmarkTest56564():
    xml_value = request.get_data(as_text=True)
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
