# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import asyncio
import urllib.parse


def BenchmarkTest05753():
    user_id = request.args.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = asyncio.run(fetch_payload())
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
