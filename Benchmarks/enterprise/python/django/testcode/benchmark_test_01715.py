# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest01715(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
