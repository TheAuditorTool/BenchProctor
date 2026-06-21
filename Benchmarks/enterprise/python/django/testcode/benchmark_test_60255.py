# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import pickle
from app_runtime import mq_client


def BenchmarkTest60255(request):
    msg_value = mq_client.get_message().body
    pending = list(str(msg_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
