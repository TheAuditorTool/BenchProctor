# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest69273(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value}'
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
