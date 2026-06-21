# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import pickle


@dataclass
class FormData:
    payload: str

def BenchmarkTest49525(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = FormData(payload=referer_value).payload
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
