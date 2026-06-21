# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import re


@dataclass
class FormData:
    payload: str

def BenchmarkTest08806(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return JsonResponse({'validated': str(data)}, status=200)
    return JsonResponse({"saved": True})
