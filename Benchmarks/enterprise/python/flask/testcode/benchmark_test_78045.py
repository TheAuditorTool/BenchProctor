# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request
import asyncio


def BenchmarkTest78045():
    upload_name = request.files['upload'].filename
    async def fetch_payload():
        await asyncio.sleep(0)
        return upload_name
    data = asyncio.run(fetch_payload())
    async def _evasion_task():
        return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
    return asyncio.run(_evasion_task())
