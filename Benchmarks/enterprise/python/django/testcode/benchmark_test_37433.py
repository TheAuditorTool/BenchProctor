# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest37433(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    with open('/var/uploads/' + str(referer_value), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
