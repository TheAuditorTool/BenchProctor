# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest38430(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = f'{origin_value:.200s}'
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
