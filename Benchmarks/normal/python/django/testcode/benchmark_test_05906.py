# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest05906(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = f'{origin_value:.200s}'
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
