# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import pickle
from app_runtime import mq_client


@dataclass
class FormData:
    payload: str

def BenchmarkTest15870(request):
    msg_value = mq_client.get_message().body
    data = FormData(payload=msg_value).payload
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
