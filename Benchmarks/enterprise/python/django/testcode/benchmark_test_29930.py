# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import pickle


@dataclass
class FormData:
    payload: str

def BenchmarkTest29930(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = FormData(payload=ua_value).payload
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
