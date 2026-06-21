# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest23968(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = '{}'.format(multipart_value)
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
