# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import os
import asyncio


def normalise_input(value):
    return value.strip()

def BenchmarkTest07410(request):
    xml_value = request.body.decode('utf-8')
    data = normalise_input(xml_value)
    async def _evasion_task():
        link_path = os.path.join('/var/app/data', str(data))
        target = os.readlink(link_path)
        with open(target, 'r') as fh:
            content = fh.read()
        return HttpResponse(content)
    return asyncio.run(_evasion_task())
