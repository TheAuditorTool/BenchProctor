# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def to_text(value):
    return str(value).strip()

def BenchmarkTest51686(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = to_text(multipart_value)
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
