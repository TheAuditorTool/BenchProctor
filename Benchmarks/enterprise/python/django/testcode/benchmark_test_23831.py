# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import pickle


@dataclass
class FormData:
    payload: str

def BenchmarkTest23831(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = FormData(payload=host_value).payload
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
