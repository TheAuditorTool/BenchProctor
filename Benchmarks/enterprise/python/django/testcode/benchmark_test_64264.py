# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest64264(request):
    multipart_value = request.POST.get('multipart_field', '')
    digest = hashlib.sha1(str(multipart_value).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
