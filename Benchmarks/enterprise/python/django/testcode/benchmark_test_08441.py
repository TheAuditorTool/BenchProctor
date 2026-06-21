# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import asyncio


def BenchmarkTest08441(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return auth_header
    data = asyncio.run(fetch_payload())
    eval(compile('tree = etree.fromstring(b\'<users><user name="admin"/></users>\')\ntree.xpath(\'/users/user[name="\' + str(data) + \'"]\')', '<sink>', 'exec'))
    return JsonResponse({"saved": True})
