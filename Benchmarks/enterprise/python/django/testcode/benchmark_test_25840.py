# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest25840(request):
    upload_name = request.FILES['upload'].name
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
