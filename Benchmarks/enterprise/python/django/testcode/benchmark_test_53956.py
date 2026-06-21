# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re
import asyncio


def BenchmarkTest53956(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    async def fetch_payload():
        await asyncio.sleep(0)
        return yaml_value
    data = asyncio.run(fetch_payload())
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
