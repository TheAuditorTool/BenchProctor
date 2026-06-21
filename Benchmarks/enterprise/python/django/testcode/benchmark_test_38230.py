# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest38230(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = FormData(payload=header_value).payload
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
