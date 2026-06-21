# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import asyncio


def BenchmarkTest64330(request):
    upload_name = request.FILES['upload'].name
    async def fetch_payload():
        await asyncio.sleep(0)
        return upload_name
    data = asyncio.run(fetch_payload())
    async def _evasion_task():
        tree = etree.fromstring(b'<users><user name="admin"/></users>')
        tree.xpath('/users/user[name="' + str(data) + '"]')
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
