# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest00221(request):
    multipart_value = request.POST.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
