# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import pickle
from app_runtime import mq_client


def BenchmarkTest78392(request):
    msg_value = mq_client.get_message().body
    data = msg_value if msg_value else 'default'
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
