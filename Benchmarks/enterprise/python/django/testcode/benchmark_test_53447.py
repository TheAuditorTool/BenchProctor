# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest53447(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
