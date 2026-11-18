# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest00606(request):
    field_value = request.POST.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
