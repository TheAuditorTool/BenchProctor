# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest00062(request):
    upload_name = request.FILES['upload'].name
    digest = hashlib.md5(str(upload_name).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
