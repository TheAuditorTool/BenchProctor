# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest00068(request):
    upload_name = request.FILES['upload'].name
    data = '%s' % (upload_name,)
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
