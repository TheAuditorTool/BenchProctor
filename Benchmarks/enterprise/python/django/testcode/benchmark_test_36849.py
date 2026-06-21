# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest36849(request):
    upload_name = request.FILES['upload'].name
    data = ' '.join(str(upload_name).split())
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
