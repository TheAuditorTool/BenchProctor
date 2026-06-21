# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
import asyncio


async def BenchmarkTest13175(request: Request):
    upload_name = (await request.form()).get('upload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return upload_name
    data = await fetch_payload()
    async def _evasion_task():
        tree = etree.fromstring(b'<users><user name="admin"/></users>')
        tree.xpath('/users/user[name="' + str(data) + '"]')
    await _evasion_task()
    return {"updated": True}
