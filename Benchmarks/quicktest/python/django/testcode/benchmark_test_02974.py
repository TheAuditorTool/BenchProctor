# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest02974(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = forwarded_ip if forwarded_ip else 'default'
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
