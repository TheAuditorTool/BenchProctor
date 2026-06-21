# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest77123(request):
    raw_body = request.body.decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
