# SPDX-License-Identifier: Apache-2.0
import os
from flask import request
import asyncio


def BenchmarkTest14223():
    origin_value = request.headers.get('Origin', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return origin_value
    data = asyncio.run(fetch_payload())
    checked_path = os.path.normpath(data)
    with open('/var/app/data/' + str(checked_path), 'r') as fh:
        content = fh.read()
    return content
