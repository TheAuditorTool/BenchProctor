# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest65465(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
