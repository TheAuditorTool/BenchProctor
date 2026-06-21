# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
import pickle
from app_runtime import mq_client


def normalise_input(value):
    return value.strip()

def BenchmarkTest46974(request):
    msg_value = mq_client.get_message().body
    data = normalise_input(msg_value)
    async def _evasion_task():
        pickle.loads(data.encode('latin-1'))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
