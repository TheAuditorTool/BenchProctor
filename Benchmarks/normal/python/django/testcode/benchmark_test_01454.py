# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest01454(request):
    upload_name = request.FILES['upload'].name
    data = '%s' % (upload_name,)
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
