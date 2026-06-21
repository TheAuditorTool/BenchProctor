# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest05361(request):
    upload_name = request.FILES['upload'].name
    data = upload_name if upload_name else 'default'
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
