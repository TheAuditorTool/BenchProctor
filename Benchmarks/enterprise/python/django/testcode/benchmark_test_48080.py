# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest48080(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
