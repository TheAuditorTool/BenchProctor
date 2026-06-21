# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest65568(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    parts = []
    for token in str(forwarded_ip).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
