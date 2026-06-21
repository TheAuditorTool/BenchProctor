# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest33690(request):
    multipart_value = request.POST.get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ','.join(parts)
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
