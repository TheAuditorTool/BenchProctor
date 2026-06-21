# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import asyncio


request_state: dict[str, str] = {}

def BenchmarkTest41000(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    async def _evasion_task():
        tree = etree.fromstring(b'<users><user name="admin"/></users>')
        tree.xpath('/users/user[name="' + str(data) + '"]')
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
