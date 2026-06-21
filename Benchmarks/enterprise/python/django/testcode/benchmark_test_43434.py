# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import asyncio


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest43434(request):
    user_id = request.GET.get('id', '')
    data = handle(user_id)
    async def _evasion_task():
        tree = etree.fromstring(b'<users><user name="admin"/></users>')
        tree.xpath('/users/user[name="' + str(data) + '"]')
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
